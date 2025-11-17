#!/usr/bin/env fish

# Build script for wenum with PyInstaller

set -x PYTHONPATH (pwd)/src

# Install dependencies
echo "[>] installing dependencies..."
pip install -e .[dev] 2>/dev/null || poetry install

# Install PyInstaller if not present
pip install pyinstaller >/dev/null 2>&1

# Clean previous builds
echo "[>] cleaning previous builds..."
rm -rf build dist *.spec.bak

# Build with PyInstaller
echo "[>] building executable with PyInstaller..."
pyinstaller wenum.spec --clean

# Check if build succeeded
if test -f dist/wenum
    echo "[>] build successful: dist/wenum"
    echo "[>] testing executable..."
    ./dist/wenum --version 2>&1 | head -1
else
    echo "[!] build failed"
    exit 1
end

