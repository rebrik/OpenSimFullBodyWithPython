#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:57:01 2018

@author: rebrik
"""

import pandas as pd
from StringIO import StringIO

def readStoFile(fpath):
    with open(fpath, 'r') as fin:
        txtIn = fin.read()
        fin.close()
      
    # find header end      
    strEndHeader = 'endheader'
    idx1 = txtIn.index(strEndHeader) + len(strEndHeader) + 1 # final \n
    txtDat = txtIn[idx1:]
    df = pd.read_csv(StringIO(txtDat), sep='\t')
    return df