#!/bin/bash
if [ -x `which python3` ]; then
    python3 ../../setup/04-setups_and_teardowns.py
else
    python ../../setup/04-setups_and_teardowns.py
fi