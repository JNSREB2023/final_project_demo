# Python Package Creation and Publishing Tutorial

A step-by-step guide to creating, testing, and publishing a Python package to PyPI using modern tools.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Creating the Package Structure](#creating-the-package-structure)
4. [Writing Your Code](#writing-your-code)
5. [Writing Tests](#writing-tests)
6. [Configuration Files](#configuration-files)
7. [Testing Your Package Locally](#testing-your-package-locally)
8. [Building the Package](#building-the-package)
9. [Publishing to TestPyPI](#publishing-to-testpypi)
10. [Publishing to PyPI](#publishing-to-pypi)
11. [Installing Your Published Package](#installing-your-published-package)

---

## Prerequisites

### Install UV
UV is a fast Python package manager. Install it first:

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:
```bash
uv --version
```

---

## Project Setup

### 1. Create Project Directory
Choose a unique package name. For this tutorial, we'll use `hello-uv-yourname` (replace `yourname` with your actual name or username).

```bash
mkdir hello-uv-yourname
cd hello-uv-yourname
```

### 2. Create Virtual Environment
```bash
uv venv
```

This creates a `.venv` folder with an isolated Python environment.

---

## Creating the Package Structure

Create the following directory structure:

```
hello-uv-yourname/
├── src/
│   └── hello_uv_yourname/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_core.py
├── pyproject.toml
├── README.md
└── LICENSE
```

### Create the directories:

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Path src\hello_uv_yourname
New-Item -ItemType Directory -Path tests
```

**macOS/Linux:**
```bash
mkdir -p src/hello_uv_yourname
mkdir tests
```

---

## Writing Your Code

### 1. Create `src/hello_uv_yourname/core.py`

```python
import numpy as np


def add_one(x):
    """Add one to a number.
    
    Args:
        x: A number
        
    Returns:
        The number plus one
    """
    return x + 1


def calculate_mean(numbers):
    """Calculate the mean of a list of numbers using numpy.
    
    Args:
        numbers: A list or array of numbers
        
    Returns:
        The mean as a float
    """
    return np.mean(numbers)
```

### 2. Create `src/hello_uv_yourname/__init__.py`

This file exposes your functions at the package level:

```python
from hello_uv_yourname.core import add_one, calculate_mean

__all__ = ["add_one", "calculate_mean"]
```

---

## Writing Tests

### Create `tests/test_core.py`

```python
from hello_uv_yourname import add_one, calculate_mean
import pytest


def test_add_one():
    assert add_one(2) == 3


mean_data = [
    ([1, 2, 3, 4, 5], 3.0),
    ([10, 20, 30], 20.0), 
    ([5], 5.0)
]


@pytest.mark.parametrize("x, expected", mean_data)
def test_calculate_mean(x, expected):
    assert calculate_mean(x) == expected
```

---

## Configuration Files

### 1. Create `pyproject.toml`

Replace `yourname` with your actual name/username and update the URLs:

```toml
[build-system]
requires = ["uv_build >= 0.9.5, <0.10.0"]
build-backend = "uv_build"

[project]
name = "hello-uv-yourname"
version = "0.1.0"
description = "A tiny demo package"
readme = "README.md"
requires-python = ">=3.8"
license = { text = "MIT" }
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent"
]
dependencies = [
    "numpy>=1.26.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/hello-uv-yourname"
Repository = "https://github.com/yourusername/hello-uv-yourname.git"
Issues = "https://github.com/yourusername/hello-uv-yourname/issues"
```

**Important Fields:**
- `name`: Must be unique on PyPI (use hyphens)
- `version`: Update this each time you publish
- `dependencies`: List all packages your code imports
- Package directory name uses underscores: `hello_uv_yourname`

### 2. Create `README.md`

```markdown
# hello-uv-yourname

A tiny demo package for learning Python packaging.

## Description

This package demonstrates:
- Basic functions (`add_one`)
- Functions with dependencies (`calculate_mean` using numpy)
- Proper project structure with tests
- Modern packaging with `uv`

## Installation

```bash
pip install hello-uv-yourname
```

## Usage

```python
from hello_uv_yourname import add_one, calculate_mean

# Add one to a number
result = add_one(5)
print(result)  # Output: 6

# Calculate mean of a list
mean = calculate_mean([1, 2, 3, 4, 5])
print(mean)  # Output: 3.0
```

## Dependencies

- Python >= 3.8
- numpy >= 1.26.0

## License

MIT
```

### 3. Create `LICENSE`

Use the MIT License (or your preferred license):

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Testing Your Package Locally

### 1. Install Your Package in Editable Mode

```bash
uv pip install -e .
```

This installs your package so Python can find it, while still allowing you to edit the code.

### 2. Install Testing Dependencies

```bash
uv pip install pytest
```

### 3. Run Your Tests

```bash
uv run pytest -q
```

You should see output like:
```
..
2 passed in 0.02s
```

### 4. Test Importing Your Package

```bash
uv run python -c "from hello_uv_yourname import add_one; print(add_one(5))"
uv run python3 -c "from test_package import add_one; print(add_one(5))"
```

---

## Building the Package

Before publishing, you need to build distribution files:

```bash
uv build
```

This creates a `dist/` folder with two files:
- `hello_uv_yourname-0.1.0.tar.gz` (source distribution)
- `hello_uv_yourname-0.1.0-py3-none-any.whl` (wheel distribution)

---

## Publishing to TestPyPI

TestPyPI is a separate instance of PyPI for testing. **Always test here first!**

### 1. Create a TestPyPI Account
- Go to https://test.pypi.org/account/register/
- Create an account and verify your email

### 2. Generate an API Token
- Log in to https://test.pypi.org/
- Go to Account Settings → API tokens
- Click "Add API token"
- Give it a name (e.g., "hello-uv-yourname")
- Set scope to "Entire account" (or specific project later)
- **Copy the token immediately** (starts with `pypi-`)

### 3. Configure Authentication

Create a `.pypirc` file in your home directory:

**Windows:** `C:\Users\YourUsername\.pypirc`
**macOS/Linux:** `~/.pypirc`

Content:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YourTestPyPITokenHere
```

**Important:** Replace `pypi-YourTestPyPITokenHere` with your actual token!

### 4. Install Twine

```bash
uv pip install twine
```

### 5. Upload to TestPyPI

```bash
uv run twine upload --repository testpypi dist/*
```

You'll see upload progress and a link to view your package, like:
```
https://test.pypi.org/project/hello-uv-yourname/0.1.0/
```

### 6. Verify on TestPyPI

Visit the link and check:
- ✅ README is displayed
- ✅ Version is correct
- ✅ Dependencies are listed
- ✅ Project URLs work

---

## Publishing to PyPI

Once you've tested on TestPyPI, you can publish to the real PyPI.

### 1. Create a PyPI Account
- Go to https://pypi.org/account/register/
- Create an account (separate from TestPyPI!)
- Verify your email

### 2. Generate PyPI API Token
- Log in to https://pypi.org/
- Go to Account Settings → API tokens
- Create a new token
- **Copy it immediately!**

### 3. Update `.pypirc`

Add the PyPI configuration:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YourActualPyPITokenHere

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YourTestPyPITokenHere
```

### 4. Upload to PyPI

```bash
uv run twine upload dist/*
```

(No `--repository` flag needed; defaults to PyPI)

Your package is now live at `https://pypi.org/project/hello-uv-yourname/`

---

## Installing Your Published Package

### From TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hello-uv-yourname
```

**Why two URLs?**
- First URL: Where your package lives (TestPyPI)
- Second URL: Where dependencies live (official PyPI)

### From Official PyPI

Once published to PyPI, anyone can install with:

```bash
pip install hello-uv-yourname
```

---

## Updating Your Package

When you make changes and want to publish an update:

### 1. Update Version Number

Edit `pyproject.toml`:
```toml
version = "0.1.1"  # Increment from 0.1.0
```

### 2. Clean Old Builds

**Windows:**
```powershell
Remove-Item dist\* -Force
```

**macOS/Linux:**
```bash
rm -rf dist/*
```

### 3. Rebuild

```bash
uv build
```

### 4. Upload

```bash
# Test first
uv run twine upload --repository testpypi dist/*

# Then to PyPI
uv run twine upload dist/*
```

**Note:** You cannot re-upload the same version number. Always increment the version!

---

## Common Issues and Solutions

### Import Error: `ModuleNotFoundError`

**Problem:** Package not installed
**Solution:** Run `uv pip install -e .`

### Twine Error: "File already exists"

**Problem:** Version already published
**Solution:** Increment version in `pyproject.toml` and rebuild

### Tests Fail with Import Errors

**Problem:** Package not installed in test environment
**Solution:** Make sure you ran `uv pip install -e .` first

### Missing README on PyPI

**Problem:** README.md is empty or not specified
**Solution:** Ensure README.md has content and `pyproject.toml` has `readme = "README.md"`

### Dependencies Not Installing

**Problem:** Dependencies not listed in `pyproject.toml`
**Solution:** Add all imported packages to the `dependencies` list

---

## Checklist

Before publishing, verify:

- [ ] All tests pass (`uv run pytest -q`)
- [ ] README.md has meaningful content
- [ ] Version number is correct and incremented
- [ ] Package name is unique (check PyPI)
- [ ] All dependencies listed in `pyproject.toml`
- [ ] LICENSE file exists
- [ ] `.pypirc` configured with API tokens
- [ ] Built successfully (`uv build`)
- [ ] Tested on TestPyPI first
- [ ] Package installs correctly from TestPyPI

---

## Additional Resources

- **UV Documentation:** https://docs.astral.sh/uv/
- **PyPI:** https://pypi.org/
- **TestPyPI:** https://test.pypi.org/
- **Python Packaging Guide:** https://packaging.python.org/
- **Semantic Versioning:** https://semver.org/

---

## Questions?

If you encounter issues:
1. Read the error message carefully
2. Check the Common Issues section above
3. Search for the error on Stack Overflow
4. Ask your instructor or classmates

Happy packaging! 🎉
