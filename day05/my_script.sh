#!/bin/sh

PYTHON=python3
LIB=virtual_env

$PYTHON -m venv $LIB

source $LIB/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

source $LIB/bin/activate