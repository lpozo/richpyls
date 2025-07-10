# Publishing to PyPI

This guide explains how to publish the `pyls` package to PyPI.

## Prerequisites

1. **PyPI Account**: Create accounts on [PyPI](https://pypi.org/account/register/) and [TestPyPI](https://test.pypi.org/account/register/)
2. **API Tokens**: Generate API tokens for both PyPI and TestPyPI
3. **Publishing Dependencies**: Install the publishing tools

## Setup

1. Install publishing dependencies:

   ```sh
   uv sync --group publish
   ```

2. Update your information in `pyproject.toml`:
   - Replace `"your-email@example.com"` with your actual email
   - Update the GitHub URLs to your repository
   - Version is automatically read from `src/pyls/__init__.py`

## Publishing Steps

### 1. Test on TestPyPI (Recommended)

```sh
# Build the package
$ uv run --group publish python -m build

# Upload to TestPyPI
$ uv run --group publish python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Test installation from TestPyPI
$ pip install --index-url https://test.pypi.org/simple/ pyls
```

### 2. Publish to PyPI

```sh
# Build the package (if not done already)
$ uv run --group publish python -m build

# Upload to PyPI
$ uv run --group publish python -m twine upload dist/*
```

### 3. Install from PyPI

```sh
pip install pyls
```

## Version Management

Before publishing:

1. Update the version in `src/pyls/__init__.py`:

   ```python
   __version__ = "0.2.0"  # Update this line
   ```

2. Create a git tag for the release:

   ```sh
   git tag v0.2.0
   git push origin v0.2.0
   ```

## Package Information

- **Package Name**: `pyls`
- **Command Name**: `pyls`
- **Module Name**: `pyls`
- **Entry Point**: `pyls:cli`

## Authentication

Use API tokens for authentication:

```sh
# Configure twine to use your API token
# Create ~/.pypirc with your tokens
```

Or use environment variables:

```sh
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=your-api-token
```
