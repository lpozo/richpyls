# Build & Publishing Guide

This document provides instructions for building and publishing the `richpyls` package.

## Building the Package

To build the package for distribution:

```sh
# Build both wheel and source distribution
uv build

# Build only wheel
uv build --wheel

# Build only source distribution
uv build --sdist

# Clean previous builds first
rm -rf dist/ && uv build
```

This creates distribution files in the `dist/` directory:

- `richpyls-X.Y.Z-py3-none-any.whl` (wheel package)
- `richpyls-X.Y.Z.tar.gz` (source distribution)

## Publishing to PyPI

### Manual Publishing

For manual publishing (though automated publishing is recommended):

```sh
# Install publishing dependencies
uv sync --group publish

# Publish to TestPyPI (for testing)
uv run twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Publish to PyPI (production)
uv run twine upload dist/*
```

### Automated Publishing

The project includes automated PyPI publishing via GitHub Actions:

```sh
# Bump version and trigger automated publishing
python bump_version.py patch  # or minor, major
git push origin main  # Triggers automated publishing

# Or use the convenience script that does everything
python bump_version.py patch --push
```

The automated workflow:

1. ✅ Runs all quality checks (formatting, linting, type checking, tests)
2. 📦 Builds and validates the package
3. 🚀 Publishes to PyPI using trusted publishing
4. 🏷️ Creates GitHub release with changelog

## PyPI Trusted Publishing Setup

To set up automated publishing:

1. **Create PyPI account** at <https://pypi.org/account/register/>
2. **Add Trusted Publisher** at <https://pypi.org/manage/account/publishing/>:
   - **Project name**: `richpyls`
   - **Owner**: `lpozo`
   - **Repository**: `richpyls`
   - **Workflow**: `publish.yml`
   - **Environment**: `pypi`
3. **Configure GitHub environment** in repository settings:
   - **Environment name**: `pypi`
   - **Protection rules**: Only `main` branch deployments

## Version Management

Update the version in `src/richpyls/__init__.py`:

```python
__version__ = "X.Y.Z"  # Update version number
```

The automated workflow will detect version changes and publish automatically when pushed to the `main` branch.
