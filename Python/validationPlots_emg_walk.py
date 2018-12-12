import pandas as pd
from readSto import readStoFile
import numpy as np 
from interpDFrame import interpDFrame
import matplotlib.pyplot as plt

# Plot simulated muscle activation vs. EMG signal

# Right Foot Strike (RFS) times
RFS1 = 0.248;
RFS2 = 1.3925;

# ------------------------------------------------------
# Import CMC states file
cmc_results_dir = '../CMC/walk/results';
cmc = readStoFile( cmc_results_dir + '/cmc_states.sto')

# Load emg activity
emg = pd.read_csv('emg_walk.txt', sep='\t')

min_time = np.amax([np.amin(cmc['time']),
                    np.amin(emg['time'])])

# recalc values as a function of the gait cycle percent
cmc_interp = interpDFrame(cmc, RFS1, RFS2, min_time)
emg_interp = interpDFrame(emg, RFS1, RFS2, min_time)

cmc_pct = cmc_interp['percentgaitcycle']
emg_pct = emg_interp['percentgaitcycle']

# ------------------------------------------------------
# Plot EMG (cyan) vs. CMC (blue) muscle activity
# magic to open plots in new window
#  %matplotlib
fig = plt.figure()
# ---------------------------------
# 1 GMAX
emgData = emg_interp['GMAX']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp[['glmax1_r/activation', 'glmax2_r/activation', 'glmax3_r/activation']].mean(axis=1)
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,1)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('gmax')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

# ---------------------------------
# 2 GMED
emgData = emg_interp['GMED']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp[['glmed1_r/activation', 'glmed2_r/activation', 'glmed3_r/activation']].mean(axis=1)
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,2)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('gmed')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

# ---------------------------------
# 3 RECFEM
emgData = emg_interp['RF']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp['recfem_r/activation']
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,3)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('recfem')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

# ---------------------------------
# 4 VASLAT
emgData = emg_interp['VL']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp['vaslat_r/activation']
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,4)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('vaslat')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

# ---------------------------------
# 5 BFLH
emgData = emg_interp['BF']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp['bflh_r/activation']
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,5)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('bflh')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

# ---------------------------------
# 6 GASLAT
emgData = emg_interp['GAS']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp['gaslat_r/activation']
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,6)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('gaslat')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

# ---------------------------------
# 7 TIBANT
emgData = emg_interp['TA']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp['tibant_r/activation']
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,7)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('tibant')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

# ---------------------------------
# 8 SOLEUS
emgData = emg_interp['SOL']
emgPlot = emgData/emgData.max()
cmcData = cmc_interp['soleus_r/activation']
cmcPlot = cmcData/cmcData.max()
ax = plt.subplot(4,2,8)
ax.plot(emg_pct, emgPlot, 'c')
ax.plot(cmc_pct, cmcPlot, 'b')
t = ax.set_title('soleus')
l = ax.set_xlim(0, 100)
l = ax.set_ylim(0, 1)

plt.show()