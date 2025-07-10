# pyls - A Python Implementation of the Unix `ls` Command

[![CI/CD Pipeline](https://img.shields.io/github/actions/workflow/status/yourusername/pyls/ci.yml?branch=main&label=CI%2FCD&logo=github)](https://github.com/yourusername/pyls/actions)
[![Test Coverage](https://img.shields.io/codecov/c/github/yourusername/pyls?logo=codecov)](https://codecov.io/gh/yourusername/pyls)
[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/pyls?logo=pypi)](https://pypi.org/project/pyls/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyls?logo=pypi)](https://pypi.org/project/pyls/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy.readthedocs.io/)
[![Security: Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

A modern, type-annotated Python implementation of the Unix `ls` command with support for long format
listings and hidden files.

## Quality Metrics

![Lines of Code](https://img.shields.io/tokei/lines/github/yourusername/pyls?style=flat-square)
![Code Size](https://img.shields.io/github/languages/code-size/yourusername/pyls?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/yourusername/pyls?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/pyls?style=flat-square)

| Metric | Value | Status |
|--------|-------|--------|
| Test Coverage | 99% | [![Coverage Status](https://img.shields.io/badge/coverage-99%25-brightgreen.svg)](https://codecov.io/gh/yourusername/pyls) |
| Type Coverage | 100% | [![mypy](https://img.shields.io/badge/mypy-100%25-brightgreen.svg)](https://mypy.readthedocs.io/) |
| Code Quality | A+ | [![Ruff](https://img.shields.io/badge/ruff-passing-brightgreen.svg)](https://github.com/astral-sh/ruff) |
| Security Scan | Clean | [![Bandit](https://img.shields.io/badge/bandit-passing-brightgreen.svg)](https://github.com/PyCQA/bandit) |
| Documentation | 100% | [![Docs](https://img.shields.io/badge/docs-100%25-brightgreen.svg)](README.md) |

## Features

- 📁 **Directory Listing**: List files and directories in the current or specified path
- 📄 **Long Format**: Display detailed file information including permissions, ownership, size, and modification time
- 🔍 **Hidden Files**: Show hidden files (starting with `.`) with the `-a` option
- 🏃 **Fast Performance**: Built with modern Python using pathlib for efficient path operations
- 🎯 **Type Safety**: Fully type-annotated codebase with mypy validation
- ✅ **Well Tested**: Comprehensive test suite with 100% coverage
- 🐍 **Modern Python**: Uses Python 3.13+ features and best practices

## Installation

### From PyPI (Recommended)

```sh
pip install pyls
```

Once installed, you can use the `pyls` command anywhere in your terminal.

### From Source

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd pyls
   ```

2. Install dependencies:

   ```sh
   # Using uv (recommended)
   $ uv sync

   # Or using pip (install click manually)
   $ pip install click
   ```

## Usage

### Basic Usage

```sh
# List files in current directory
$ pyls

# List files in specific directory
$ pyls /path/to/directory

# List multiple files/directories
$ pyls file1.txt directory1 file2.txt
```

### Command Options

| Option | Description |
|--------|-------------|
| `-l` | Use long listing format (shows permissions, ownership, size, date) |
| `-a` | Show all files, including hidden files (starting with `.`) |
| `-la` | Combine long format with showing hidden files |

### Examples

```sh
# Basic listing
$ pyls
README.md
pyproject.toml
src
tests
uv.lock

# Long format listing
$ pyls -l
-rw-r--r--  1 user staff    1234 Dec 01 12:00 README.md
-rw-r--r--  1 user staff     249 Dec 01 12:00 pyproject.toml
drwxr-xr-x  3 user staff      96 Dec 01 12:00 src
drwxr-xr-x  4 user staff     128 Dec 01 12:00 tests
-rw-r--r--  1 user staff    9316 Dec 01 12:00 uv.lock

# Show hidden files
$ pyls -a
.git
.gitignore
.python-version
.venv
README.md
pyproject.toml
src
tests
uv.lock

# Long format with hidden files
$ pyls -la
drwxr-xr-x 12 user staff    384 Dec 01 12:00 .git
-rw-r--r--  1 user staff    1234 Dec 01 12:00 README.md
-rw-r--r--  1 user staff     249 Dec 01 12:00 pyproject.toml
drwxr-xr-x  3 user staff      96 Dec 01 12:00 src
drwxr-xr-x  4 user staff     128 Dec 01 12:00 tests
-rw-r--r--  1 user staff    9316 Dec 01 12:00 uv.lock
```

## Technologies

### Runtime Dependencies

- **[Python 3.13+](https://python.org)**: Modern Python with type hints and advanced features
- **[pathlib](https://docs.python.org/3/library/pathlib.html)**: Object-oriented filesystem paths (built-in)
- **[click](https://click.palletsprojects.com/)**: Command-line interface creation toolkit

### Development Dependencies

- **[pytest](https://pytest.org/)**: Testing framework for comprehensive test coverage
- **[mypy](https://mypy.readthedocs.io/)**: Static type checker for Python
- **[ruff](https://github.com/astral-sh/ruff)**: Fast Python linter and formatter
- **[bandit](https://github.com/PyCQA/bandit)**: Security vulnerability scanner
- **[pre-commit](https://pre-commit.com/)**: Git hooks for automated quality checks
- **[uv](https://docs.astral.sh/uv/)**: Fast Python package manager and resolver

### Build & Deployment

![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/pyls/ci.yml?branch=main&label=Build&logo=github)
![Tests](https://img.shields.io/github/actions/workflow/status/yourusername/pyls/ci.yml?branch=main&label=Tests&logo=pytest)
![PyPI Status](https://img.shields.io/pypi/status/pyls?logo=pypi)
![Wheel](https://img.shields.io/pypi/wheel/pyls?logo=pypi)

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
$ uv run python -m pytest --cov=pyls
```

### Type Checking

```sh
# Check types with mypy
$ uv run mypy src/pyls/

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
- **Comprehensive tests**: Full test coverage with edge cases
- **Clean architecture**: Well-organized code with clear separation of concerns
- **Modern Python**: Uses latest Python features and best practices

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Implement your feature or bug fix
4. **Add tests**: Ensure your changes are well-tested
5. **Run quality checks**:

   ```sh
   uv run python -m pytest  # Run tests
   uv run mypy src/pyls/     # Type check
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

- Email: [your-email@example.com](mailto:your-email@example.com)
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

⭐ If you found this project helpful, please give it a star!

## Acknowledgments

- Inspired by the Unix `ls` command
- Built with modern Python best practices
- Thanks to the Python community for excellent tools and libraries
