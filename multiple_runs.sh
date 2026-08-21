#!/bin/bash

#this is a bash script that runs 5 repeat reframe likwid tests 
#see lbm_runonly.py for exact test/executable
#then it runs the python3 script that reads the csv file and outputs readable data

#save this in the LBM-Bench directory alongside the executable lbmbench-GCC-dp	

rm perflogs/generic/default/lbm_test.log

reframe -c lbm_runonly.py --repeat 5 -r

python3 perflogs/generic/default/analysis.py
