#!/bin/bash
./run_autoformat.sh
mypy .
pytest . --pylint -m pylint --pylint-rcfile=.python_starter_pylintrc
pytest tests/
