"""A file for initializing the repository.

This file should be deleted after initial setup.
"""

import json
import shutil
import subprocess
from pathlib import Path


def _git_replace(old: str, new: str) -> None:
    subprocess.run(
        [
            "git",
            "grep",
            "-l",
            f'"{old}"',
            "|",
            "xargs",
            "sed",
            "-i",
            "''",
            "-e",
            f'"s/{old}/{new}/g"',
        ],
        check=True,
    )


def _main() -> None:
    # Parse the config.
    config_file = Path(".").parent / "config.json"
    assert config_file.exists(), "Missing config file"
    with open(config_file, "r", encoding="utf-8") as fp:
        config = json.load(fp)

    # Validate the config.
    assert "developer" in config, "Missing developer name in config file"
    github_username = config["github-username"]
    assert not " " in github_username, "Malformed GitHub username"
    package_name = config["your-package-name"]
    assert (
        " " not in package_name
    ), "Package names cannot contain spaces (you want to `import package_name`)"
    assert (
        "-" not in package_name
    ), "Package names cannot dashes (you want to `import package_name`)"
    python_version = config["python-version"]
    assert python_version.startswith("3"), "Only Python 3 is supported"
    assert python_version.startswith(
        "3."
    ), "Missing dot in Python version (example: 3.10)"
    python_subversion = python_version.split(".")[1]
    assert python_subversion.isdigit()

    # Get the repository name from this directory.
    repo_name = Path(".").parent.resolve().name

    # Delete the existing git files if they are from the starter repo.
    git_repo = Path(".").parent / ".git"
    if git_repo.exists():
        git_config_file = git_repo / "config"
        with open(git_config_file, "r", encoding="utf-8") as fp:
            git_config_contents = fp.read()
        if "git@github.com:tomsilver/python-starter.git" in git_config_contents:
            shutil.rmtree(git_repo)

    # Initialize the repo anew.
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)

    # Replace all occurrences of default names.
    substitutions = {
        "tomsilver": github_username,
        "python-starter": repo_name,
        "python_starter": package_name,
        "3.10": f"3.{python_subversion}",
        "310": f"3{python_subversion}",
    }
    for old, new in substitutions.items():
        _git_replace(old, new)

    # Rename the package repo.
    subprocess.run(["mv", "src/python_starter", f"src/{package_name}"], check=True)

    # Commit and push.
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "First commit"], check=True)
    subprocess.run(
        [
            "git",
            "remote",
            "add",
            "origin",
            f"git@github.com:{github_username}/{repo_name}.git",
        ],
        check=True,
    )
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)


if __name__ == "__main__":
    _main()
