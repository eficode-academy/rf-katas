#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`/setup
if [ -x `which python3` ]; then
    python3 setup/05-negative_testing.py
else
    python setup/05-negative_testing.py
fi