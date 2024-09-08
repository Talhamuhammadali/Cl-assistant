#!/bin/bash

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/venv/bin/activate"
export PYTHONPATH="$DIR:$PYTHONPATH"
python -m core.v1.cli "$@"
deactivate