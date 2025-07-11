# Badge Configuration

This document describes all the badges used in the README.md and their purposes.

## Status Badges

### CI/CD & Build Status

- **CI/CD Pipeline**: Shows the status of the GitHub Actions workflow
- **Build Status**: Shows if the package builds successfully
- **Tests**: Shows if all tests are passing

### Code Quality

- **Test Coverage**: Shows percentage of code covered by tests (from Codecov)
- **Code Style**: Shows that code follows Ruff formatting standards
- **Type Checking**: Shows that code is fully type-annotated with mypy
- **Security**: Shows that code passes security scans with Bandit
- **Pre-commit**: Shows that pre-commit hooks are enabled

### Package Information

- **Python Version**: Shows minimum Python version requirement (3.13+)
- **PyPI Version**: Shows the latest version available on PyPI
- **PyPI Downloads**: Shows monthly download count from PyPI
- **License**: Shows the project license (MIT)

### Repository Metrics

- **Lines of Code**: Total lines of code in the repository
- **Code Size**: Size of the codebase
- **Repository Size**: Total repository size
- **Last Commit**: Date of the most recent commit

## Badge URLs

**Note**: Replace `lpozo/pyls` with your actual GitHub repository path if different.

### Primary Badges (Top of README)

```markdown
[![CI/CD Pipeline](https://img.shields.io/github/actions/workflow/status/lpozo/pyls/ci.yml?branch=main&label=CI%2FCD&logo=github)](https://github.com/lpozo/pyls/actions)
[![Test Coverage](https://img.shields.io/codecov/c/github/lpozo/pyls?logo=codecov)](https://codecov.io/gh/lpozo/pyls)
[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/pyls?logo=pypi)](https://pypi.org/project/pyls/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyls?logo=pypi)](https://pypi.org/project/pyls/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy.readthedocs.io/)
[![Security: Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
```

### Quality Metrics (Quality Metrics Section)

```markdown
![Lines of Code](https://img.shields.io/tokei/lines/github/yourusername/pyls?style=flat-square)
![Code Size](https://img.shields.io/github/languages/code-size/yourusername/pyls?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/yourusername/pyls?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/pyls?style=flat-square)
```

### Build & Deployment (Technologies Section)

```markdown
![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/pyls/ci.yml?branch=main&label=Build&logo=github)
![Tests](https://img.shields.io/github/actions/workflow/status/yourusername/pyls/ci.yml?branch=main&label=Tests&logo=pytest)
![PyPI Status](https://img.shields.io/pypi/status/pyls?logo=pypi)
![Wheel](https://img.shields.io/pypi/wheel/pyls?logo=pypi)
```

## Badge Services

- **[Shields.io](https://shields.io/)**: Primary badge service for most badges
- **[Codecov](https://codecov.io/)**: Test coverage reporting and badges
- **[GitHub Actions](https://github.com/features/actions)**: CI/CD status badges
- **[PyPI](https://pypi.org/)**: Package version and download statistics

## Customization

### Colors

- **Green**: Success, passing, high quality (brightgreen, green)
- **Blue**: Information, versions, tools (blue)
- **Yellow**: Warnings, licenses, security (yellow)
- **Red**: Failures, errors (red)

### Logos

Most badges include relevant logos (github, pypi, codecov, pytest, etc.) for better visual identification.

## Maintenance

1. **Repository URLs**: Update all `lpozo/pyls` references when repository is published
2. **Package Name**: Update `pyls` references if package name changes
3. **Workflow Names**: Ensure workflow file names match badge URLs
4. **Version Numbers**: PyPI badges update automatically when new versions are published
5. **Coverage**: Codecov badges update automatically when coverage reports are uploaded

## Optional Badges

Additional badges that could be added:

```markdown
[![GitHub Issues](https://img.shields.io/github/issues/lpozo/pyls)](https://github.com/lpozo/pyls/issues)
[![GitHub Stars](https://img.shields.io/github/stars/lpozo/pyls)](https://github.com/lpozo/pyls/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/lpozo/pyls)](https://github.com/lpozo/pyls/network)
[![Contributors](https://img.shields.io/github/contributors/lpozo/pyls)](https://github.com/lpozo/pyls/graphs/contributors)
```
