# Build Instructions

## Python 3.13 Compatibility Fixes

Fixed two compatibility issues:
1. **cgi module removal**: Replaced `cgi.parse_header()` with manual header parsing in `src/wenum/externals/reqresp/Response.py`
2. **pkg_resources deprecation**: Replaced with `importlib.resources` in `src/wenum/helpers/file_func.py`

## Uninstall Old Version

```fish
pipx uninstall wenum
```

## Install Locally

```fish
cd /work
pip install -e .
# or with poetry
poetry install
```

## Test Fixes

```fish
python3 test_fixes.py
```

## Build Standalone Executable

```fish
./build.sh
```

This creates `dist/wenum` - a standalone executable.

## Manual Build Steps

```fish
# Install dependencies
pip install pyinstaller
poetry install  # or: pip install -e .

# Build
pyinstaller wenum.spec --clean

# Test
./dist/wenum --version
```

## GitHub Release

1. Tag release:
```fish
git tag -a v0.1.1 -m "Python 3.13 compatibility fixes"
git push origin v0.1.1
```

2. Create release on GitHub, upload `dist/wenum` binary.

