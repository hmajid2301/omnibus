import abc
from typing import Generic, TypeVar

T = TypeVar("T")


class AbstractRepository(abc.ABC, Generic[T]):
    @abc.abstractmethod
    async def add(self, doc: T):
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, id_: str) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    async def remove(self, id_: str):
        raise NotImplementedError
