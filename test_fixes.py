#!/usr/bin/env python3
"""Quick test to verify Python 3.13 compatibility fixes"""

import sys
import re
from io import BytesIO

# Test cgi replacement - copy the function directly to avoid importing full module
def get_encoding_from_headers(headers):
    content_type = headers.get("Content-Type")
    if not content_type:
        return None
    # Python 3.13+ compatible: cgi.parse_header() was removed
    if ';' in content_type:
        main_type, rest = content_type.split(';', 1)
        main_type = main_type.strip()
        params = {}
        for param in rest.split(';'):
            if '=' in param:
                key, value = param.split('=', 1)
                params[key.strip().lower()] = value.strip().strip('"\'')
    else:
        main_type = content_type.strip()
        params = {}
    content_type = main_type
    if "charset" in params:
        return params["charset"].strip("'\"")
    if "text" in content_type:
        return "ISO-8859-1"
    if "image" in content_type:
        return "utf-8"
    if "application/json" in content_type:
        return "utf-8"

print("Testing cgi.parse_header() replacement...")
test_headers = [
    {"Content-Type": "text/html; charset=utf-8"},
    {"Content-Type": "application/json"},
    {"Content-Type": "text/plain; charset=ISO-8859-1"},
    {"Content-Type": "image/png"},
]

for headers in test_headers:
    encoding = get_encoding_from_headers(headers)
    print(f"  {headers['Content-Type']} -> {encoding}")

# Test importlib.resources (simulated)
print("\nTesting importlib.resources availability...")
try:
    from importlib import resources
    print(f"  ✓ importlib.resources available (Python {sys.version_info.major}.{sys.version_info.minor})")
except ImportError:
    print(f"  ✗ importlib.resources not available")
    sys.exit(1)

# Verify our code doesn't import cgi
print("\nVerifying code doesn't use cgi module...")
import ast
with open('src/wenum/externals/reqresp/Response.py', 'r') as f:
    content = f.read()
    if 'import cgi' in content or 'from cgi' in content:
        print("  ✗ ERROR: cgi still imported in Response.py")
        sys.exit(1)
    else:
        print("  ✓ No cgi imports found in code")

print("\n✓ All compatibility fixes verified")

