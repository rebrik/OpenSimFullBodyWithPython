#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:57:29 2018

@author: rebrik
"""

import subprocess
process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
out, err = process.communicate()
print(out)

proc = subprocess.Popen(['./printNumbers.sh'], 
                        shell=False, bufsize=1, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT)
while (True):
    # Read line from stdout, print, break if EOF reached
    line = proc.stdout.readline()
    line = line.decode()
    if (line == ""): break
    print line,
    
proc.poll()   
    
from simFunctions import runProgram

rc = runProgram(['./printNumbers.sh'])
print 'Return code: ', rc

    