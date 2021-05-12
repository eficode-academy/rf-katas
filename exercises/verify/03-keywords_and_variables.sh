#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`/setup
if [ -x `which python3` ]; then
    python3 setup/03-keywords_and_variables.py
else
    python setup/03-keywords_and_variables.py
fi