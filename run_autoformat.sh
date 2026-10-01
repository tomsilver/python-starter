#!/bin/bash
set -e
ruff check --select I --fix .
python -m black .
# Docformatter exits with 3 when it reformats a file successfully.
docformatter -i -r . --exclude venv || [ "$?" -eq 3 ]
