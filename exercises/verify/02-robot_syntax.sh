#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`/setup
if [ -x `which python3` ]; then
    python3 setup/02-robot_syntax.py
else
    python setup/01-robot_syntax.py
fi