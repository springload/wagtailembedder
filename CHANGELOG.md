# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

...

## [1.2] - 2018-04-04

### Added

- Compatibility with Python 3.5 and 3.6

### Changed

- Now licensed under MIT
- The snippet button isn't enabled by default anymore. Add `snippet` to the list of features of your `RichTextBlock`s and `RichTextField`s to show the button or use the `register_rich_text_features` to register it as a default feature with `features.default_features.append('snippet')`.

### Removed

- Compatibility with Python 2.6, 3.2 and 3.3
- Compatibility with Wagtail prior 1.12

## [1.1] - 2016-07-04

### Fixed

- Compatibility with Wagtail 1.4 (really)

## [1.0] - 2016-05-02

### Fixed

- Compatibility with Wagtail 1.4

## [0.1.5] - 2016-02-15

### Fixed

- Compatibility with Wagtail 1.3.1

### Removed

- Compatibility prior to Wagtail 1.3.1

## [0.1.4] - 2015-07-07

### Fixed

- Wheel and build properly

## [0.1.2] - 2015-04-1

### Fixed

- Some bugs

## [0.1.1] - 2015-01-27

### Fixed

- Some bugs

### Changed

- CSS improved
- Exceptions properly handled

## [0.1] - 2015-01-23

Initial Release

[Unreleased]: https://github.com/springload/wagtailembedder/compare/1.2...HEAD
[1.1]: https://github.com/springload/wagtailembedder/compare/1.1...1.2
[1.1]: https://github.com/springload/wagtailembedder/compare/1.0...1.1
[1.0]: https://github.com/springload/wagtailembedder/compare/0.1.5...1.0
[0.1.5]: https://github.com/springload/wagtailembedder/compare/0.1.4...0.1.5
[0.1.4]: https://github.com/springload/wagtailembedder/compare/0.1.2...0.1.4
[0.1.2]: https://github.com/springload/wagtailembedder/compare/v0.1.1...0.1.2
[0.1.1]: https://github.com/springload/wagtailembedder/compare/v0.1...v0.1.1
[0.1]: https://github.com/springload/wagtailembedder/compare/ef3f0ff68eda48c90fc1c5cd2411fa67cc54e52d...v0.1
