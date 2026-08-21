#!/bin/bash

rm perflogs/generic/default/lbm_test.log

reframe -c lbm_runonly.py --repeat 5 -r

python3 perflogs/generic/default/analysis.py
