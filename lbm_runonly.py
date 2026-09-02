# Copyright 2016-2024 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause
import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.builtins import sanity_function, performance_function


@rfm.simple_test
class lbm_test(rfm.RunOnlyRegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    #executable = '/cosma/home/do018/dc-huan3/LBM-Bench/lbmbench-GCC-dp'
    executable = 'likwid-perfctr -C 0,1 -g L3 /cosma/home/do018/dc-huan3/LBM-Bench/lbmbench-GCC-dp'
    #-C is no. threads, -g is performance group
    #change the executable file path, other executable options are eg. lbmbench-CLANG-dp etc.
    time_limit = '1h'

    @sanity_function
    def validate(self):
        return sn.assert_found(r'Evaluation Stats', self.stdout)

    @performance_function('s')
    def runtime_bw(self):
        return sn.extractsingle(r'runtime:\s+(\S+)', self.stdout, 1, float)

    @performance_function('MFLUP/s')
    def performance_bw(self):
        return sn.extractsingle(r'performance:\s+(\S+)', self.stdout, 1, float)

    @performance_function('GByte/s')
    def bandwidth_bw(self):
        return sn.extractsingle(r'MEM bandwidth:\s+(\S+)', self.stdout, 1, float)

    @performance_function('MHz')
    def clockfreq_bw(self):
        return sn.extractsingle(r'Clock \[MHz\]\s+\|\s+(\S+)', self.stdout, 1, float)
        
    @performance_function('MBytes/s')
    def accessbandwidth_bw(self):
        return sn.extractsingle(r'L3 access bandwidth \[MBytes/s\]\s+\|\s+(\S+)', self.stdout, 1, float)

    @performance_function('GBytes')
    def accessdatavolume_bw(self):
        return sn.extractsingle(r'L3 access data volume \[GBytes\]\s+\|\s+(\S+)', self.stdout, 1, float)

    @performance_function('%')
    def accessrate_bw(self):
        return sn.extractsingle(r'L3 access rate \[%\]\s+\|\s+(\S+)', self.stdout, 1, float)

    @performance_function('%')
    def missrate_bw(self):
        return sn.extractsingle(r'L3 miss rate \[%\]\s+\|\s+(\S+)', self.stdout, 1, float)

    @performance_function('%')
    def missratio_bw(self):
        return sn.extractsingle(r'L3 miss ratio \[%\]\s+\|\s+(\S+)', self.stdout, 1, float)




