#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`/setup
if [ -x `which python3` ]; then
    python3 setup/06-resource_files.py
else
    python setup/06-resource_files.py
fi