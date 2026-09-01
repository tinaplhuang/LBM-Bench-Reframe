#!/bin/bash

rm perflogs/generic/default/lbm_test.log
#deleting old logs incase we use a different number of reruns etc, LBM usually will just append new runs


reframe -c lbm_runonly.py --repeat 5 -r

python3 perflogs/generic/default/analysis.py
#calling the formatting python script
#note the directory structure, analysis.py needs to be in that location
