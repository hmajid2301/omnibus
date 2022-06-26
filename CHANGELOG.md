# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [0.3.0] - 2022-06-26
### Changed
- Updated packages

## [0.2.6] - 2022-02-15
### Changed
- Typing on `document_models` to not be optional.

## [0.2.5] - 2022-02-14
### Changed
- Typing on `document_models` if `None` to be empty list

## [0.2.4] - 2022-02-14
### Changed
- Separate `UVICORN_LOG_LEVEL` env variable for logs.

## [0.2.3] - 2022-02-05
### Changed
- Upgraded `uvicorn` to `0.17.4` and use standard which is required by `core-api`.

### Fixed
- `use_route_names_as_operation_ids` called directly by the services that use this library. Need to be imported after all routes have been imported.

## [0.2.2] - 2022-01-09
### Fixed
- Not calling `setup_logger`.

## [0.2.1] - 2022-01-04
### Changed
- refactor `JWTBearer`, removing redundant if, else check. Should never end up with empty credentials.

## [0.2.0] - 2022-01-03
### Added
- `auth` module to handle authentication and authorisation using JWT bearer tokens.

## [0.1.1] - 2021-12-31
### Changed
- Set default values in arguments of `UvicornTestServer` rather than constants.

## [0.1.0] - 2021-12-31
### Added
- Initial Release.

[unreleased]: https://gitlab.com/banter-bus/omnibus/compare/0.3.0...main
[0.3.0]: https://gitlab.com/banter-bus/omnibus/compare/0.3.0...0.2.6
[0.2.6]: https://gitlab.com/banter-bus/omnibus/compare/0.2.6...0.2.5
[0.2.5]: https://gitlab.com/banter-bus/omnibus/compare/0.2.5...0.2.4
[0.2.4]: https://gitlab.com/banter-bus/omnibus/compare/0.2.4...0.2.3
[0.2.3]: https://gitlab.com/banter-bus/omnibus/compare/0.2.3...0.2.2
[0.2.2]: https://gitlab.com/banter-bus/omnibus/compare/0.2.2...0.2.1
[0.2.1]: https://gitlab.com/banter-bus/omnibus/compare/0.2.1...0.2.0
[0.2.0]: https://gitlab.com/banter-bus/omnibus/compare/0.2.0...0.1.1
[0.1.1]: https://gitlab.com/banter-bus/omnibus/compare/0.1.1...0.1.0
[0.1.0]: https://gitlab.com/banter-bus/omnibus/-/tags/0.1.0
