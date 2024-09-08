#!/bin/bash

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Path to your Python script that generates completions
PYTHON_SCRIPT="$DIR/core/v2/assistant.py"

ai() {
    local completions
    
    # Activate the virtual environment
    source "$DIR/venv/bin/activate"

    # Activate env, Retrieve completion, deactivate env
    export PYTHONPATH="$DIR:$PYTHONPATH"
    completions=$(python3 "$PYTHON_SCRIPT" "$@")
    deactivate

    # Print the completions
    echo "$completions"
}

_ai_completions()
{
    local cur prev words cword
    _init_completion || return
    local completions
    completions=$(ai "${words[@]:1}")
    COMPREPLY=($(compgen -W "$completions" -- "$cur"))
}

# Register the completion function
complete -F _ai_completions ai