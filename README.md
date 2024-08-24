# Python Starter Repo

![workflow](https://github.com/tomsilver/python-starter/actions/workflows/ci.yml/badge.svg)

A basic template for building Python packages.

## Features
- **Easy to install** with `pip install -e .` (see `pyproject.toml`)
- **Continuous integration** with GitHub Actions (see `.github/workflows/ci.yml` and `run_ci_checks.sh`)
- **Autoformatting** with black, isort, and docformatter (see `run_autoformat.sh`)
- **Linting** with pytest-pylint (see `.pylintrc`)
- **Type checking** with mypy (see `pyproject.toml`)
- **Unit tests** with pytest (see `tests/`)

## Instructions

### Create an Empty Repository on GitHub
1. Go to https://github.com/new and follow the instructions on the first page. No need to include a .gitignore, README, or LICENSE; these will be added later. After the first click, stop -- don't follow the command line instructions. Remember the NAME of the repository and then go on to step 2.

### Set Up the Code
2. **Clone this repository** and give it the name of your repository: `git clone git@github.com:tomsilver/python-starter.git <NAME>`. You should now have a directory called NAME. **Enter** that directory: `cd <NAME>`.
3. **Configure the repository:** Make changes to `config.json` and then save.
4. **Apply the configuration**: Run `python apply_configuration.py`.

:tada: **That's it! Your code is ready to use** :tada: You should see your code back on GitHub where you previously had an empty repository.

### Common Next Steps
5. **Make changes** to `pyproject.toml`, especially in the dependencies section.
6. **Install your repository**: `pip install -e .` (recommended: use a virtualenv).
7. **Replace the starter files** (`README.md`, `LICENSE`, `config.json`, `apply_configuration.py`, `structs.py`, `utils.py` and the analogous files in `tests/`) with some of your own.

### Configure GitHub (Optional but Recommended)
8. **Set up branch protections** to prevent accidental changes to your main branch. In `https://github.com/<USER>/<NAME>/settings/branches`:
    - Click `Add classic branch protection rule`.
    - The branch pattern name is `main`.
    - Check "Require a pull request before merging (optionally: uncheck "Require approvals").
    - Check "Require status checks to pass before merging".
    - Check "Require branches to be up to date before merging".
    - Then type in `autoformat`, `static-type-checking`, `linting`, `unit-tests`.
    - Check "Do not allow bypassing the above settings".
9. **Set up repository settings** in `https://github.com/$MYGITUSER$/$MYREPO/settings`:
    - Check "Allow auto-merge".
    - Check "Automatically delete head branches".
    - Uncheck "Allow merge commits".
    - Uncheck "Allow rebase merging".
10. **Set up contributor settings** to lower the barrier for external contributions. In `https://github.com/$MYGITUSER$/$MYREPO/settings/actions`:
    - Update "Fork pull request workflows from outside collaborators" to "Require approval for first-time contributors who are new to GitHub".


## Notes
- Continuous integration with GitHub Actions only works if you have a public repository or an Enterprise account. You can still run checks locally with `./run_ci_checks.sh` regardless.
- You can include your repository as a dependency if it's hosted on GitHub. For example, alongside requirements like `numpy` or `matplotlib` in a `pyproject.toml` or `requirements.txt` or `setup.py`, you can list `"YOUR-PACKAGE-NAME@git+https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME.git"`.
- Feel free to open pull requests to improve this repository.
- You can use this code and modify it in any way without any attributions or acknowledgements (see `LICENSE`).
