# Publishing to PyPI

This guide explains how to publish the `pyls` package to PyPI, including both automated and manual publishing methods.

## 🤖 Automated Publishing (Recommended)

### Overview

The project includes automated PyPI publishing via GitHub Actions. When you push a version change to the main branch, the package is automatically:

1. ✅ **Quality checked** (formatting, linting, type checking, tests)
2. 📦 **Built and validated**
3. 🚀 **Published to PyPI**
4. 🏷️ **Tagged and released** on GitHub

### Quick Start

1. **Update the version** in `src/pyls/__init__.py`:

   ```python
   __version__ = "0.2.0"  # Increment as needed
   ```

2. **Commit and push** to main:

   ```sh
   git add src/pyls/__init__.py
   git commit -m "bump: version 0.2.0"
   git push origin main
   ```

3. **Wait for automation** - The GitHub Actions workflow will handle the rest!

### Setup Requirements

#### PyPI Trusted Publishing (Secure - No API tokens needed!)

1. Go to [PyPI Trusted Publishing](https://pypi.org/manage/account/publishing/)
2. Add a new trusted publisher:
   - **PyPI Project Name**: `pyls`
   - **Owner**: `yourusername`
   - **Repository**: `pyls`
   - **Workflow**: `publish.yml`
   - **Environment**: `pypi`

See [AUTOMATED_PUBLISHING.md](AUTOMATED_PUBLISHING.md) for detailed setup instructions.

## 📖 Manual Publishing

For manual publishing or testing purposes:

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
