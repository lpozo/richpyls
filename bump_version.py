#!/usr/bin/env python3
"""Version bump utility for pyls package.

This script helps automate version bumping and follows semantic versioning.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def get_current_version() -> str:
    """Get the current version from __init__.py."""
    init_file = Path("src/pyls/__init__.py")
    if not init_file.exists():
        raise FileNotFoundError("Could not find src/pyls/__init__.py")

    content = init_file.read_text()
    match = re.search(r'__version__ = "([^"]+)"', content)
    if not match:
        raise ValueError("Could not find __version__ in __init__.py")

    return match.group(1)


def bump_version(current_version: str, bump_type: str) -> str:
    """Bump version according to semantic versioning."""
    parts = current_version.split(".")
    if len(parts) != 3:
        raise ValueError(f"Invalid version format: {current_version}")

    major, minor, patch = map(int, parts)

    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")

    return f"{major}.{minor}.{patch}"


def update_version_file(new_version: str) -> None:
    """Update the version in __init__.py."""
    init_file = Path("src/pyls/__init__.py")
    content = init_file.read_text()

    # Replace the version
    new_content = re.sub(
        r'__version__ = "[^"]+"', f'__version__ = "{new_version}"', content
    )

    init_file.write_text(new_content)
    print(f'Updated src/pyls/__init__.py: __version__ = "{new_version}"')


def run_tests() -> bool:
    """Run tests to ensure everything works."""
    try:
        print("Running tests...")
        result = subprocess.run(
            ["uv", "run", "python", "-m", "pytest", "--cov=pyls", "-q"],
            capture_output=True,
            text=True,
            check=True,
        )
        print("✅ Tests passed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False


def check_code_quality() -> bool:
    """Run code quality checks."""
    checks = [
        (["uv", "run", "ruff", "format", "--check", "."], "Code formatting"),
        (["uv", "run", "ruff", "check", "."], "Code linting"),
        (["uv", "run", "mypy", "src/pyls/"], "Type checking"),
    ]

    for cmd, name in checks:
        try:
            print(f"Running {name}...")
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ {name} passed")
        except subprocess.CalledProcessError as e:
            print(f"❌ {name} failed: {e}")
            return False

    return True


def git_commit_and_tag(version: str, push: bool = False) -> None:
    """Commit the version change and create a git tag."""
    try:
        # Add the changed file
        subprocess.run(["git", "add", "src/pyls/__init__.py"], check=True)

        # Commit the change
        commit_msg = f"bump: version {version}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"✅ Committed version bump: {commit_msg}")

        # Create tag
        tag_name = f"v{version}"
        subprocess.run(["git", "tag", tag_name], check=True)
        print(f"✅ Created tag: {tag_name}")

        if push:
            # Push changes and tags
            subprocess.run(["git", "push", "origin", "main"], check=True)
            subprocess.run(["git", "push", "origin", tag_name], check=True)
            print("✅ Pushed changes and tags to origin")
            print("🚀 Automated publishing workflow will now trigger!")
        else:
            print("💡 Run 'git push origin main' to trigger automated publishing")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Bump version for pyls package")
    parser.add_argument(
        "bump_type", choices=["major", "minor", "patch"], help="Type of version bump"
    )
    parser.add_argument(
        "--skip-tests", action="store_true", help="Skip running tests before bumping"
    )
    parser.add_argument(
        "--skip-quality",
        action="store_true",
        help="Skip code quality checks before bumping",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Automatically push changes and trigger publishing",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    args = parser.parse_args()

    try:
        # Get current version
        current_version = get_current_version()
        new_version = bump_version(current_version, args.bump_type)

        print(f"Current version: {current_version}")
        print(f"New version: {new_version}")

        if args.dry_run:
            print("🏃 Dry run mode - no changes will be made")
            print(
                f"Would bump {args.bump_type} version: {current_version} → {new_version}"
            )
            return

        # Run quality checks
        if not args.skip_quality:
            if not check_code_quality():
                print(
                    "❌ Code quality checks failed. Fix issues before bumping version."
                )
                sys.exit(1)

        # Run tests
        if not args.skip_tests:
            if not run_tests():
                print("❌ Tests failed. Fix tests before bumping version.")
                sys.exit(1)

        # Update version
        update_version_file(new_version)

        # Git commit and tag
        git_commit_and_tag(new_version, args.push)

        print(f"🎉 Successfully bumped version to {new_version}")

        if not args.push:
            print("\n📋 Next steps:")
            print("   git push origin main  # Trigger automated publishing")
            print("   # Or run with --push to do this automatically")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
