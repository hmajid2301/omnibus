from typing import Optional

from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from google.auth.transport import requests
from google.oauth2 import id_token


class JWTBearer(HTTPBearer):
    def __init__(self, client_id: str) -> None:
        self.client_id = client_id
        super(JWTBearer, self).__init__(auto_error=True)

    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        credentials = await super(JWTBearer, self).__call__(request=request)
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={"error_message": "unknown authorization error", "error_code": "auth_error"},
            )

        try:
            token = credentials.credentials
            id_token.verify_oauth2_token(token, requests.Request(), self.client_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"error_message": "invalid JWT token", "error_code": "auth_error"},
            )
        return credentials
