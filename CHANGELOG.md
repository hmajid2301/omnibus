# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2021-01-04
### Changed
- refactor `JWTBearer`, removing redundant if, else check. Should never end up with empty credentials.

## [0.2.0] - 2021-01-03
### Added
- `auth` module to handle authentication and authorisation using JWT bearer tokens.

## [0.1.1] - 2021-12-31
### Changed
- Set default values in arguments of `UvicornTestServer` rather than constants.

## [0.1.0] - 2021-12-31
### Added
- Initial Release.

[unreleased]: https://gitlab.com/banter-bus/omnibus/compare/0.2.0...main
[0.2.0]: https://gitlab.com/banter-bus/omnibus/compare/0.2.0...0.1.1
[0.1.1]: https://gitlab.com/banter-bus/omnibus/compare/0.1.1...0.1.0
[0.1.0]: https://gitlab.com/banter-bus/omnibus/-/tags/0.1.0
