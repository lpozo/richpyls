# Code Quality Guide

This project uses several tools to maintain high code quality and consistency.

## Available Tools

### 🔧 Ruff - Code Formatting and Linting

Ruff is our primary tool for code formatting and linting, providing fast Python linting and formatting.

**Commands:**

```sh
# Format code
$ uv run ruff format .

# Lint code and show issues
$ uv run ruff check .

# Lint and auto-fix issues
$ uv run ruff check . --fix

# Check specific files
$ uv run ruff check src/pyls/__main__.py
```

**Configuration:** Ruff is configured in `pyproject.toml` under `[tool.ruff]`.

### 🔍 MyPy - Type Checking

MyPy provides static type checking to catch type-related errors.

**Commands:**

```sh
# Type check the main package
$ uv run mypy src/pyls/

# Type check all Python files
$ uv run mypy .

# Type check with verbose output
$ uv run mypy src/pyls/ --verbose
```

**Configuration:** MyPy uses the default configuration, relying on type annotations in the code.

### 🧪 Pytest - Testing

Pytest runs our comprehensive test suite with coverage reporting.

**Commands:**

```sh
# Run all tests
$ uv run python -m pytest

# Run tests with coverage
$ uv run python -m pytest --cov=pyls

# Run tests with verbose output
$ uv run python -m pytest -v

# Run specific test
$ uv run python -m pytest tests/test_pyls.py::test_default_and_show_all
```

### 🔒 Bandit - Security Scanning

Bandit scans for common security issues in Python code.

**Commands:**

```sh
# Run security scan
$ uv run bandit -r src/

# Run with configuration from pyproject.toml
$ uv run bandit -c pyproject.toml -r src/
```

## Pre-commit Hooks

Pre-commit hooks automatically run quality checks before each commit.

### Setup

Pre-commit is already installed and configured. The hooks will run automatically on every `git commit`.

### Manual Execution

```sh
# Run pre-commit on all files
$ uv run pre-commit run --all-files

# Run pre-commit on staged files only
$ uv run pre-commit run

# Update pre-commit hook versions
$ uv run pre-commit autoupdate
```

### Hooks Configured

1. **ruff-format**: Auto-formats Python code
2. **ruff**: Lints Python code and auto-fixes issues
3. **mypy**: Type checking
4. **trailing-whitespace**: Removes trailing whitespace
5. **end-of-file-fixer**: Ensures files end with a newline
6. **check-toml**: Validates TOML file syntax
7. **check-merge-conflict**: Checks for merge conflict markers
8. **check-added-large-files**: Prevents large files from being committed
9. **mixed-line-ending**: Ensures consistent line endings
10. **bandit**: Security scanning
11. **markdownlint**: Markdown linting and formatting

## GitHub Actions CI/CD

The project includes automated CI/CD workflows that run on every push and pull request.

### Workflows

1. **Code Quality** (`lint-and-format` job):
   - Runs ruff formatting check
   - Runs ruff linting
   - Runs mypy type checking

2. **Test Suite** (`test` job):
   - Runs pytest with coverage
   - Uploads coverage to Codecov

3. **Build Package** (`build` job):
   - Builds the package
   - Validates the built package
   - Uploads build artifacts

### Workflow Files

- `.github/workflows/ci.yml`: Main CI/CD pipeline

## Configuration Files

- `pyproject.toml`: Contains configuration for ruff, bandit, pytest, and build system
- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `.markdownlint.json`: Markdown linting rules

## Development Workflow

1. **Make changes** to the code
2. **Run tests** to ensure functionality: `uv run python -m pytest`
3. **Format code** with ruff: `uv run ruff format .`
4. **Check linting** with ruff: `uv run ruff check .`
5. **Type check** with mypy: `uv run mypy src/pyls/`
6. **Commit changes** - pre-commit hooks will run automatically
7. **Push to GitHub** - CI/CD pipeline will run automatically

## Quality Standards

The project maintains high quality standards:

- **99% test coverage** - All code should be tested
- **Type annotations** - All functions and variables should be type-annotated
- **Ruff compliance** - Code should pass all ruff checks
- **Security scanning** - No security issues should be present
- **Documentation** - All public APIs should be documented

## Troubleshooting

### Pre-commit Hook Failures

If pre-commit hooks fail:

1. Review the error messages
2. Fix the issues manually or let auto-fixers handle them
3. Stage the fixed files: `git add .`
4. Commit again: `git commit -m "Your message"`

### Ruff Issues

If ruff reports issues:

1. Try auto-fixing first: `uv run ruff check . --fix`
2. For remaining issues, fix them manually
3. For false positives, consider adding `# noqa: RULE_CODE` comments

### MyPy Type Errors

If mypy reports type errors:

1. Add missing type annotations
2. Fix type mismatches
3. Use `# type: ignore` comments sparingly for unavoidable issues

### Test Failures

If tests fail:

1. Run tests with verbose output: `uv run python -m pytest -v`
2. Fix the failing functionality
3. Ensure all tests pass before committing
