#!/bin/bash
# Build script for richpyls package

set -e

echo "🏗️  Building richpyls package..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Install build dependencies
echo "📦 Installing build dependencies..."
uv sync --group publish

# Run tests
echo "🧪 Running tests..."
uv run --group dev python -m pytest

# Type checking
echo "🔍 Running type checks..."
uv run --group dev mypy src/richpyls/

# Build the package
echo "📦 Building package..."
uv run --group publish python -m build

# Verify the build
echo "✅ Package built successfully!"
echo "📁 Built files:"
ls -la dist/

echo ""
echo "🚀 Ready to publish!"
echo "   Test: uv run python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*"
echo "   Live: uv run python -m twine upload dist/*"
