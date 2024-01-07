#!/bin/sh
cd `dirname $0`

VENV_NAME=".venv"
PYTHON="$VENV_NAME/bin/python"
ENTRYPOINT="src/"

if [ -f .installed ]
    then
        # Skip  virtual environment creation if it already exists
        source $VENV_NAME/bin/activate
    else
        # Create virtual environment and activate it to run the code
        python3 -m venv $VENV_NAME
        source $VENV_NAME/bin/activate
        $PYTHON -m pip install -r requirements/prod.txt -U
        if [ $? -eq 0 ]
            then
                touch .installed
        fi
fi

# Executes code
exec $PYTHON $ENTRYPOINT $@
