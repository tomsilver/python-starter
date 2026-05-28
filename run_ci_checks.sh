#!/bin/bash
set -e
./run_autoformat.sh
mypy .
pytest . --pylint -m pylint --pylint-rcfile=.pylintrc
pytest tests/
