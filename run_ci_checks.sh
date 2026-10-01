#!/bin/bash
set -e
./run_autoformat.sh
mypy .
ruff check .
pytest tests/
