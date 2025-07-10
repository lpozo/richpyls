# pyls - A Python Implementation of the Unix `ls` Command

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy.readthedocs.io/)

A modern, type-annotated Python implementation of the Unix `ls` command with support for long format listings and hidden files.

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

```bash
pip install pyls
```

Once installed, you can use the `pyls` command anywhere in your terminal.

### From Source

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd pyls
   ```

2. Install dependencies:

   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip (install click manually)
   pip install click
   ```

## Usage

### Basic Usage

```bash
# List files in current directory
pyls

# List files in specific directory
pyls /path/to/directory

# List multiple files/directories
pyls file1.txt directory1 file2.txt
```

### Command Options

| Option | Description |
|--------|-------------|
| `-l` | Use long listing format (shows permissions, ownership, size, date) |
| `-a` | Show all files, including hidden files (starting with `.`) |
| `-la` | Combine long format with showing hidden files |

### Examples

```bash
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
- **[uv](https://docs.astral.sh/uv/)**: Fast Python package manager and resolver

## Development

### Setup

1. Clone the repository and navigate to the project directory
2. Install development dependencies:

   ```bash
   uv sync --dev
   ```

3. Activate the virtual environment:

   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

### Running Tests

```bash
# Run all tests
uv run python -m pytest

# Run tests with verbose output
uv run python -m pytest -v

# Run tests with coverage
uv run python -m pytest --cov=pyls
```

### Type Checking

```bash
# Check types with mypy
uv run mypy src/pyls/

# Check all Python files
uv run mypy .
```

### Code Quality

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

   ```bash
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
