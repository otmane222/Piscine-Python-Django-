#!/bin/sh

PYTHON=python3
LIB=local_lib

$PYTHON -m venv $LIB

source $LIB/bin/activate

pip install --upgrade pip

pip install -r requirement.txt

source $LIB/bin/activate