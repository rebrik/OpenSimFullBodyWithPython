#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 18:21:46 2018

@author: rebrik
"""
import pandas as pd
import numpy as np 
from  scipy import interpolate

def interpDFrame( dfIn, tRFS1, tRFS2, min_time ):
# first column is time, others are dependencies on time

    t_cycle = tRFS2 - tRFS1
    t_marg = t_cycle * 0.0
    max_time1 = min_time + t_cycle + t_marg
    min_time1 = min_time - t_marg
    
    # remove rows which are beyond full gait cycle
    df1 = dfIn[(dfIn['time']>=min_time1)&(dfIn['time']<=max_time1)].copy()
    time = df1['time'].values
    
    t1 = (time-tRFS1)*100/t_cycle
    df1['percentgaitcycle'] = pd.Series(t1, index=df1.index)
    
    # modulo 100 percentgaitcycle
    pm = np.mod(df1['percentgaitcycle'],100.0)
    df1['pm'] = pd.Series(pm, index=df1.index)
    
    # order by percentgaitcycle mod
    df2 = df1.sort_values('pm')
    pm = df2['pm'] # ordered pm
    # we will interpolate non-time columns
    df3 = df2.drop(['time','percentgaitcycle','pm'], axis=1)
    
    cycleGrid = pd.Series(np.arange(0.0, 100.0))
    cycleGrid.name = 'percentgaitcycle'
    dfInterp=pd.DataFrame(cycleGrid)

    for colName in df3.columns:
        # interp function for x-y pair
        interpFunc = interpolate.interp1d(pm, df3[colName], fill_value='extrapolate')
        # calc values on the grid
        colInterp = pd.Series(interpFunc(cycleGrid))
        dfInterp[colName] = colInterp
    
    return dfInterp




