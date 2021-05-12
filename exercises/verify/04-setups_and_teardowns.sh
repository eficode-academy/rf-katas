#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`/setup
if [ -x `which python3` ]; then
    python3 setup/04-setups_and_teardowns.py
else
    python setup/04-setups_and_teardowns.py
fi