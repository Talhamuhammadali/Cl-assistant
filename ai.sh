#!/bin/bash

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Activate the virtual environment
source "$DIR/venv/bin/activate"

# Run the Python script with any arguments passed to this shell script
python -m core.cli "$@"

# Deactivate the virtual environment
deactivate