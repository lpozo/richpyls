# Automated PyPI Publication Setup Guide

This guide explains how to set up automated PyPI publication for the `pyls` package.

## Overview

The automated publication system will:

1. **Trigger on version changes** in the main branch
2. **Run all quality checks** before publishing
3. **Publish to PyPI** using trusted publishing (secure, no API tokens needed)
4. **Create GitHub releases** automatically
5. **Handle failures gracefully** with proper notifications

## Setup Requirements

### 1. PyPI Trusted Publishing Configuration

**Trusted Publishing** is the most secure way to publish to PyPI from GitHub Actions. No API tokens needed!

#### Steps to Configure

1. **Go to PyPI**: <https://pypi.org/manage/account/publishing/>
2. **Add a new trusted publisher** with these details:
   - **PyPI Project Name**: `pyls`
   - **Owner**: `lpozo` (your GitHub username)
   - **Repository name**: `pyls`
   - **Workflow filename**: `publish.yml`
   - **Environment name**: `pypi` (optional but recommended)

3. **Save the configuration**

### 2. GitHub Repository Settings

#### Environment Protection (Recommended)

1. Go to **Settings > Environments** in your GitHub repository
2. Create a new environment named `pypi`
3. Add protection rules:
   - **Required reviewers**: Add yourself for manual approval
   - **Deployment branches**: Restrict to `main` branch only

#### Secrets (Alternative to Trusted Publishing)

If you prefer using API tokens instead of trusted publishing:

1. Generate a PyPI API token at <https://pypi.org/manage/account/token/>
2. Add it as a repository secret named `PYPI_API_TOKEN`

## Workflow Features

### Automated Triggers

The workflow triggers on:

- **Push to main branch** with version changes
- **Manual dispatch** for emergency releases
- **Only when source files change** (not documentation-only changes)

### Quality Gates

Before publishing, the workflow ensures:

- ✅ **Code formatting** passes (Ruff)
- ✅ **Linting** passes (Ruff)
- ✅ **Type checking** passes (mypy)
- ✅ **All tests** pass with high coverage
- ✅ **Security scan** passes (Bandit)
- ✅ **Package build** succeeds
- ✅ **Package validation** passes

### Version Detection

The workflow automatically detects version changes by:

1. Comparing the current commit with the previous one
2. Checking if `src/pyls/__init__.py` was modified
3. Verifying that the `__version__` variable changed
4. Only publishing if a version bump is detected

### Release Creation

After successful publication, the workflow:

1. **Creates a Git tag** with the version number
2. **Creates a GitHub release** with release notes
3. **Includes installation instructions**
4. **Lists all quality checks that passed**

## Usage Workflow

### Standard Release Process

1. **Make your changes** and ensure all tests pass locally
2. **Update the version** in `src/pyls/__init__.py`:

   ```python
   __version__ = "0.2.0"  # Increment as needed
   ```

3. **Commit and push** to main:

   ```sh
   git add src/pyls/__init__.py
   git commit -m "bump: version 0.2.0"
   git push origin main
   ```

4. **Workflow runs automatically** and publishes if all checks pass

### Emergency Release

For urgent fixes, you can trigger publication manually:

1. Go to **Actions > Publish to PyPI** in your GitHub repository
2. Click **Run workflow**
3. Select the `main` branch
4. Click **Run workflow**

### Hotfix Process

For hotfixes that need immediate release:

1. Create the fix
2. Bump the patch version (e.g., `0.1.0` → `0.1.1`)
3. Push to main
4. Workflow publishes automatically

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (`1.0.0`): Breaking changes
- **MINOR** (`0.1.0`): New features, backward compatible
- **PATCH** (`0.0.1`): Bug fixes, backward compatible

Examples:

```python
__version__ = "0.1.0"  # Initial release
__version__ = "0.1.1"  # Bug fix
__version__ = "0.2.0"  # New feature
__version__ = "1.0.0"  # Major release
```

## Security Features

### Trusted Publishing Benefits

- ✅ **No API tokens** to manage or rotate
- ✅ **Short-lived credentials** generated automatically
- ✅ **Repository-specific** permissions
- ✅ **Audit trail** in both GitHub and PyPI
- ✅ **Revocable** access without token management

### Environment Protection

- 🛡️ **Manual approval** for production releases
- 🛡️ **Branch restrictions** to main only
- 🛡️ **Time delays** for additional review time
- 🛡️ **Required reviewers** for sensitive operations

## Monitoring and Notifications

### Success Indicators

- ✅ **Green workflow status** in GitHub Actions
- ✅ **New release** appears in GitHub Releases
- ✅ **Package version** updated on PyPI
- ✅ **Download badge** reflects new version

### Failure Handling

- ❌ **Workflow fails** if any quality check fails
- ❌ **No publication** if tests don't pass
- ❌ **Email notifications** on workflow failures
- ❌ **Slack/Discord** integration possible for team notifications

## Troubleshooting

### Common Issues

#### "Package already exists"

- Check if version was already published
- Ensure version was actually incremented
- Use `workflow_dispatch` to retry with new version

#### "Permission denied"

- Verify trusted publishing configuration
- Check repository settings match PyPI configuration
- Ensure environment protection rules are correct

#### "Quality checks failed"

- Review failed step in GitHub Actions
- Fix the issue locally and test
- Commit fix with version bump

#### "No version change detected"

- Ensure `__version__` in `src/pyls/__init__.py` was modified
- Check that the change is in the commit being pushed
- Verify file path and variable name are correct

### Debug Steps

1. **Check workflow logs** in GitHub Actions
2. **Verify version change** in the commit
3. **Test locally** with same commands
4. **Check PyPI status** page for service issues
5. **Review trusted publishing** configuration

## Best Practices

### Development Workflow

1. **Feature branches** for development
2. **Pull requests** for code review
3. **Version bumps** only in main branch
4. **Test everything** before version bump
5. **Descriptive commit** messages for releases

### Version Management

1. **Plan releases** and version increments
2. **Document changes** in commit messages
3. **Test pre-release** versions when needed
4. **Coordinate** team releases
5. **Monitor download** statistics

### Security Practices

1. **Use trusted publishing** instead of API tokens
2. **Enable environment protection** for production
3. **Regular audit** of publishing permissions
4. **Monitor release** notifications
5. **Review workflow** changes carefully

## Configuration Files

The automated publication system uses these files:

- `.github/workflows/publish.yml`: Main publication workflow
- `pyproject.toml`: Package configuration and dependencies
- `src/pyls/__init__.py`: Version source of truth

All files are configured and ready to use!
