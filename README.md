# dev

Contains helpful scripts for development.

- [checkBuild](#checkbuild)

## checkBuild

A script which can be used to check build artifacts for various unwanted
stuff.

The following functions will:

- `__check_architectures`: if the artifact contains only the valid architectures
- `__check_coverage_symbols`: if the artifact contains code coverage symbols
- `__check_profiling_data`: if the artifact contains profiling symbols
- `__check_encryption`: if encryption information is present
- `__check_bitcode_available`: if bitcode is enabled
- `__check_for_assertion`: if the artifact contains assertion symbols
- `__check_debug_symbols`: if the artifact contains debug symbols
