# richpyls - A Python Implementation of the Unix `ls` Command

[![CI/CD Pipeline](https://img.shields.io/github/actions/workflow/status/lpozo/richpyls/ci.yml?branch=main&label=CI%2FCD&logo=github)](https://github.com/lpozo/richpyls/actions)
[![Test Coverage](https://img.shields.io/codecov/c/github/lpozo/richpyls?logo=codecov)](https://codecov.io/gh/lpozo/richpyls)
[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/richpyls?logo=pypi)](https://pypi.org/project/richpyls/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/richpyls?logo=pypi)](https://pypi.org/project/richpyls/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy.readthedocs.io/)
[![Security: Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

A modern, type-annotated Python implementation of the Unix `ls` command with beautiful Rich formatting,
color-coded file types, and support for long format listings and hidden files.

## Quality Metrics

![Lines of Code](https://img.shields.io/tokei/lines/github/lpozo/richpyls?style=flat-square)
![Code Size](https://img.shields.io/github/languages/code-size/lpozo/richpyls?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/lpozo/richpyls?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/lpozo/richpyls?style=flat-square)

| Metric | Value | Status |
|--------|-------|--------|
| Test Coverage | 89% | [![Coverage Status](https://img.shields.io/badge/coverage-89%25-brightgreen.svg)](https://codecov.io/gh/lpozo/richpyls) |
| Type Coverage | 100% | [![mypy](https://img.shields.io/badge/mypy-100%25-brightgreen.svg)](https://mypy.readthedocs.io/) |
| Code Quality | A+ | [![Ruff](https://img.shields.io/badge/ruff-passing-brightgreen.svg)](https://github.com/astral-sh/ruff) |
| Security Scan | Clean | [![Bandit](https://img.shields.io/badge/bandit-passing-brightgreen.svg)](https://github.com/PyCQA/bandit) |
| Documentation | 100% | [![Docs](https://img.shields.io/badge/docs-100%25-brightgreen.svg)](README.md) |

## Features

- 🎨 **Rich Visual Output**: Beautiful color-coded file types with emoji icons
- 📁 **Directory Listing**: List files and directories in the current or specified path
- 📄 **Long Format**: Display detailed file information in a professional table format
- 🌳 **Tree View**: Display directories in a tree-like hierarchical format with the `-t` option
- 🔍 **Hidden Files**: Show hidden files (starting with `.`) with the `-a` option using 🫣 emoji
- 🏃 **Fast Performance**: Built with modern Python using pathlib for efficient path operations
- 🎯 **Type Safety**: Fully type-annotated codebase with mypy validation
- ✅ **Well Tested**: Comprehensive test suite with 89% coverage
- 🐍 **Modern Python**: Uses Python 3.13+ features and best practices

## File Type Icons

The Rich output includes beautiful emoji icons for different file types:

- 🐍 Python files (`.py`, `.pyx`, `.pyi`)
- ⚙️ Configuration files (`.toml`, `.json`, `.yaml`, `.yml`, `.ini`, `.cfg`, `.conf`)
- 📄 Documentation files (`.md`, `.rst`, `.txt`, `.doc`, `.docx`, `.pdf`)
- 📦 Archive files (`.zip`, `.tar`, `.gz`, `.bz2`, `.xz`, `.7z`, `.rar`)
- 🖼️ Image files (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.svg`, `.ico`)
- 📁 Directories
- ⚡ Executable files
- 🔗 Symbolic links
- 🫣 Hidden files (starting with `.`)

## Installation

### From PyPI (Recommended)

```sh
pip install richpyls
```

Once installed, you can use the `richpyls` command anywhere in your terminal.

### From Source

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd richpyls
   ```

2. Install dependencies:

   ```sh
   # Using uv (recommended)
   $ uv sync

   # Or using pip (install Rich and Click manually)
   $ pip install rich click
   ```

## Usage

### Basic Usage

```sh
# List files in current directory
$ richpyls

# List files in specific directory
$ richpyls /path/to/directory

# List multiple files/directories
$ richpyls file1.txt directory1 file2.txt
```

### Command Options

| Option | Description |
|--------|-------------|
| `-l` | Use long listing format (shows permissions, ownership, size, date in Rich table) |
| `-a` | Show all files, including hidden files (starting with `.`) with 🫣 emoji |
| `-t` | Display directories in a tree-like format with Rich styling |
| `-la` | Combine long format with showing hidden files |
| `-tl` | Combine tree format with long listing |
| `-ta` | Combine tree format with showing hidden files |

### Examples

```sh
# Basic listing with Rich icons and colors
$ richpyls
📄 README.md
⚙️ pyproject.toml
📁 src
📁 tests
📄 uv.lock

# Long format listing with Rich table
$ richpyls -l
                                     📁 Directory Listing
┏━━━━┳━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━
┃ T… ┃ Permissio… ┃ Links ┃ Owner     ┃ Group    ┃     Size ┃ Modified     ┃ Name
┡━━━━╇━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━
│ 📄 │ -rw-r--r-- │     1 │ user      │ staff    │   1.2KB  │ Dec 01 12:00 │ 📄 READ…
│ ⚙️  │ -rw-r--r-- │     1 │ user      │ staff    │    249B  │ Dec 01 12:00 │ ⚙️ pypro…
│ 📁 │ drwxr-xr-x │     3 │ user      │ staff    │     96B  │ Dec 01 12:00 │ 📁 src
│ 📁 │ drwxr-xr-x │     4 │ user      │ staff    │    128B  │ Dec 01 12:00 │ 📁 tests
│ 📄 │ -rw-r--r-- │     1 │ user      │ staff    │   9.3KB  │ Dec 01 12:00 │ 📄 uv.lo
└────┴────────────┴───────┴───────────┴──────────┴──────────┴──────────────┴─────────

# Show hidden files with special emoji
$ richpyls -a
🫣 .git
🫣 .gitignore
🫣 .python-version
📁 .venv
📄 README.md
⚙️ pyproject.toml
📁 src
📁 tests
📄 uv.lock

# Tree format (shows directory structure with Rich styling)
$ richpyls -t
├── 📄 README.md
├── ⚙️ pyproject.toml
├── 📁 src
│   └── 📁 richpyls
│       ├── 🐍 __init__.py
│       └── 🐍 __main__.py
├── 📁 tests
│   ├── 🐍 __init__.py
│   └── 🐍 test_richpyls.py
└── 📄 uv.lock

# Tree format with long listing and Rich table
$ richpyls -tl src
└── 📁 src
                                     📁 Directory Listing
┏━━━━┳━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━
┃ T… ┃ Permissio… ┃ Links ┃ Owner     ┃ Group    ┃     Size ┃ Modified     ┃ Name
┡━━━━╇━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━
│ 📁 │ drwxr-xr-x │     3 │ user      │ staff    │     96B  │ Dec 01 12:00 │ 📁 richpyls
└────┴────────────┴───────┴───────────┴──────────┴──────────┴──────────────┴─────────
    ├── 🐍 __init__.py
    └── 🐍 __main__.py
```

## Technologies

### Runtime Dependencies

- **[Python 3.13+](https://python.org)**: Modern Python with type hints and advanced features
- **[pathlib](https://docs.python.org/3/library/pathlib.html)**: Object-oriented filesystem paths (built-in)
- **[click](https://click.palletsprojects.com/)**: Command-line interface creation toolkit
- **[rich](https://rich.readthedocs.io/)**: Rich text and beautiful formatting for the terminal

### Development Dependencies

- **[pytest](https://pytest.org/)**: Testing framework for comprehensive test coverage
- **[mypy](https://mypy.readthedocs.io/)**: Static type checker for Python
- **[ruff](https://github.com/astral-sh/ruff)**: Fast Python linter and formatter
- **[bandit](https://github.com/PyCQA/bandit)**: Security vulnerability scanner
- **[pre-commit](https://pre-commit.com/)**: Git hooks for automated quality checks
- **[uv](https://docs.astral.sh/uv/)**: Fast Python package manager and resolver

### Build & Deployment

![Build Status](https://img.shields.io/github/actions/workflow/status/lpozo/richpyls/ci.yml?branch=main&label=Build&logo=github)
![Tests](https://img.shields.io/github/actions/workflow/status/lpozo/richpyls/ci.yml?branch=main&label=Tests&logo=pytest)
![PyPI Status](https://img.shields.io/pypi/status/richpyls?logo=pypi)
![Wheel](https://img.shields.io/pypi/wheel/richpyls?logo=pypi)

## Development

### Setup

1. Clone the repository and navigate to the project directory
2. Install development dependencies:

   ```sh
   uv sync --dev
   ```

3. Set up pre-commit hooks for code quality:

   ```sh
   uv run pre-commit install
   ```

4. Activate the virtual environment:

   ```sh
   $ source .venv/bin/activate  # On macOS/Linux
   # or
   $ .venv\Scripts\activate     # On Windows
   ```

### Running Tests

```sh
# Run all tests
$ uv run python -m pytest

# Run tests with verbose output
$ uv run python -m pytest -v

# Run tests with coverage
$ uv run python -m pytest --cov=richpyls
```

### Type Checking

```sh
# Check types with mypy
$ uv run mypy src/richpyls/

# Check all Python files
$ uv run mypy .
```

### Code Quality and Formatting

The project uses automated code quality tools:

```sh
# Format code with ruff
$ uv run ruff format .

# Lint code with ruff
$ uv run ruff check . --fix

# Security scan with bandit
$ uv run bandit -r src/
```

**Pre-commit hooks** automatically run quality checks on every commit. See
[CODE_QUALITY.md](CODE_QUALITY.md) for detailed information about all quality tools and workflows.

### Building the Package

To build the package for distribution:

```sh
# Build both wheel and source distribution
$ uv build

# Build only wheel
$ uv build --wheel

# Build only source distribution
$ uv build --sdist

# Clean previous builds first
$ rm -rf dist/ && uv build
```

This creates distribution files in the `dist/` directory:

- `richpyls-X.Y.Z-py3-none-any.whl` (wheel package)
- `richpyls-X.Y.Z.tar.gz` (source distribution)

### Publishing to PyPI

For manual publishing (though automated publishing is recommended):

```sh
# Install publishing dependencies
$ uv sync --group publish

# Publish to TestPyPI (for testing)
$ uv run twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Publish to PyPI (production)
$ uv run twine upload dist/*
```

### Automated Publishing

The project includes automated PyPI publishing via GitHub Actions:

```sh
# Bump version and trigger automated publishing
$ python bump_version.py patch  # or minor, major
$ git push origin main  # Triggers automated publishing

# Or use the convenience script that does everything
$ python bump_version.py patch --push
```

The automated workflow:

1. ✅ Runs all quality checks (formatting, linting, type checking, tests)
2. 📦 Builds and validates the package
3. 🚀 Publishes to PyPI using trusted publishing
4. 🏷️ Creates GitHub release with changelog

See [AUTOMATED_PUBLISHING.md](AUTOMATED_PUBLISHING.md) for setup instructions.

### Project Standards

The project maintains high code quality through:

- **Type annotations**: All functions and variables are type-annotated
- **Comprehensive tests**: 89% test coverage with edge cases
- **Clean architecture**: Well-organized code with clear separation of concerns
- **Modern Python**: Uses latest Python features and best practices
- **Rich UI**: Beautiful terminal output with colors, icons, and professional formatting

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Implement your feature or bug fix
4. **Add tests**: Ensure your changes are well-tested
5. **Run quality checks**:

   ```sh
   uv run python -m pytest  # Run tests
   uv run mypy src/richpyls/     # Type check
   ```

6. **Commit your changes**: `git commit -m 'Add amazing feature'`
7. **Push to the branch**: `git push origin feature/amazing-feature`
8. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints to all new code
- Write tests for new functionality
- Update documentation as needed
- Ensure all tests pass before submitting

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

### Leodanis Pozo Ramos

- GitHub: [@lpozo](https://github.com/lpozo)

---

⭐ If you found this project helpful, please give it a star!

## Acknowledgments

- Inspired by the Unix `ls` command
- Built with modern Python best practices
- Thanks to the Python community for excellent tools and libraries
- Special thanks to the [Rich](https://rich.readthedocs.io/) library for beautiful terminal output
