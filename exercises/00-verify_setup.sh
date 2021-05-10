#!/bin/bash
if [ -x `which python3` ]; then
    python3 ../setup/verify_env.py
else
    python ../setup/verify_env.py
fi