#!/bin/bash
if [ -x `which python3` ]; then
    python3 ../setup/07-test_template.py
else
    python ../setup/07-test_template.py
fi
