#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`/setup
if [ -x `which python3` ]; then
    python3 setup/01-manual_testing.py
else
    python setup/01-manual_testing.py
fi