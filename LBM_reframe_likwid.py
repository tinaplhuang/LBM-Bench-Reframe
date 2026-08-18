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
    executable = 'likwid-pin -c N:0 /cosma/home/do018/dc-huan3/LBM-Bench/lbmbench-GCC-dp'
    #Change file path to filepath of benchmark to make it run
    time_limit='1h'

    @sanity_function
    def validate(self):
        return sn.assert_found(r'Evaluation Stats', self.stdout)

    @performance_function('s')
    def copy_bw(self):
        return sn.extractsingle(r'runtime:\s+(\S+)', self.stdout, 1, float)

    @performance_function('MFLUP/s')
    def performance_bw(self):
        return sn.extractsingle(r'performance:\s+(\S+)',self.stdout,1,float)
    @performance_function('GByte/s')
    def bandwidth_bw(self):
        return sn.extractsingle(r'MEM bandwidth:\s+(\S+)', self.stdout, 1, float)
