#!/bin/sh

LOG_FILE="install_log.log"
PYTHON_LATEST="python3.9"
VENV_PATH="local_lib"
PATH_PATH_PY="https://github.com/jaraco/path.git"


if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH"
fi

# activate venv
source $VENV_PATH/bin/activate

# pip version
pip --version | awk '{print $1 " " $2}'

if [ ! -d "$VENV_PATH/lib/$PYTHON_LATEST/site-packages/path" ]; then
    pip install --log $LOG_FILE --force-reinstall  git+$PATH_PATH_PY 
fi

# run my_program.py

python3 my_program.py

