import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from readSto import readStoFile
from interpDFrame import interpDFrame

def sumCMC(dfCMC):
    col_list= list(dfCMC)
    col_list.remove('time')
    colOut = df[col_list].sum(axis=1)
    return colOut

# walk, free-speed
id_results_dir = '../ID/results_walk';
cmc_results_dir = '../CMC/walk/results';

# Right Foot Strike (RFS) times
RFS1 = 0.248;
RFS2 = 1.3925;

# ---------------------------------------------------------
# Load simulation outputs from file, 
# normalize time to % gait cycle,
# and calculate net muscle-generated joint moments

#----------------------------------------------------------
# ID
id_filename = id_results_dir +'/inverse_dynamics.sto'

df = readStoFile(id_filename)
#df.columns

# put columns of interest into a new dataframe 
time = df['time']
# min time is the same for id and cmc
min_time = np.amin(time)
hipflex = df['hip_flexion_r_moment']
hipflex.name = 'hipflex'
kneeext = -df['knee_angle_r_moment'] 
kneeext.name = 'kneeext' 
ankleext = -df['ankle_angle_r_moment'] 
ankleext.name = 'ankleext'

# make dataframe from the id joint moments
idJointMoments = pd.concat([time, hipflex, kneeext, ankleext], axis=1)
idJointMoments_interp = interpDFrame(idJointMoments, RFS1, RFS2, min_time)

#plt.plot(idJointMoments_interp['percentgaitcycle'], idJointMoments_interp['hipflex'], '-')
#plt.show()

#----------------------------------------------------------
# Hip flexion moment (CMC, Muscle Analysis)
fname = cmc_results_dir + '/cmc_MuscleAnalysis_Moment_hip_flexion_r.sto'
df = readStoFile(fname)
time = df['time']
hipflex = sumCMC(df)
hipflex.name = 'hipflex'

# Knee *extension* moment (CMC, Muscle Analysis)
fname = cmc_results_dir + '/cmc_MuscleAnalysis_Moment_knee_angle_r.sto'
df = readStoFile(fname)
kneeext = -sumCMC(df)
kneeext.name = 'kneeext' 

# Ankle *extension* moment (CMC, Muscle Analysis)
fname = cmc_results_dir + '/cmc_MuscleAnalysis_Moment_ankle_angle_r.sto'
df = readStoFile(fname)
ankleext = -sumCMC(df)
ankleext.name = 'ankleext'

cmcJointMoments = pd.concat([time, hipflex, kneeext, ankleext], axis=1)
cmcJointMoments_interp = interpDFrame(cmcJointMoments, RFS1, RFS2, min_time)

#  
#plt.figure
#plt.plot(idJointMoments_interp['percentgaitcycle'], idJointMoments_interp['hipflex'], '*b')
#plt.plot(cmcJointMoments_interp['percentgaitcycle'], idJointMoments_interp['hipflex'], '+r')
#plt.show()

# magic to open plots in new window
#  %matplotlib

fig = plt.figure()
ax1 = plt.subplot(3,1,1)
ax2 = plt.subplot(3,1,2)
ax3 = plt.subplot(3,1,3)

# ------------------------------------------------------
# Plot ID joint moments
ax1.plot(idJointMoments_interp['percentgaitcycle'], idJointMoments_interp['hipflex'], 'b')
ax2.plot(idJointMoments_interp['percentgaitcycle'], idJointMoments_interp['kneeext'], 'b')
ax3.plot(idJointMoments_interp['percentgaitcycle'], idJointMoments_interp['ankleext'], 'b')

# ------------------------------------------------------
# Plot CMC muscle-generated joint moments
ax1.plot(cmcJointMoments_interp['percentgaitcycle'], cmcJointMoments_interp['hipflex'], 'r')
ax2.plot(cmcJointMoments_interp['percentgaitcycle'], cmcJointMoments_interp['kneeext'], 'r')
ax3.plot(cmcJointMoments_interp['percentgaitcycle'], cmcJointMoments_interp['ankleext'], 'r')

# ------------------------------------------------------
# Label plots
ax1.set(ylabel='hip flexion moment')
ax1.set(xlim=[0,100])
ax1.set(ylim=[-100,100])

ax2.set(ylabel='knee extension moment')
ax2.set(xlim=[0,100])
ax2.set(ylim=[-100,100])

ax3.set(ylabel='ankle plantarflexion moment')
ax3.set(xlim=[0,100])
ax3.set(ylim=[-50,150])

plt.xlabel('percent gait cycle')


# ------------------------------------------------------
# Compute RMS and peak errors between CMC and muscle-generated joint moments
matID = idJointMoments_interp.values[:,1:4]
maxID = np.amax(matID, axis=0) 

matCMC = cmcJointMoments_interp.values[:,1:4]
maxCMC = np.amax(matCMC, axis = 0)

matDiff = np.subtract(matID, matCMC)
rms_id_cmc = np.sqrt(np.mean(matDiff**2, axis = 0))

peak_id_cmc = np.amax(np.abs(matDiff), axis = 0)

rms_id_cmc_norm = rms_id_cmc/maxID
peak_id_cmc_norm = peak_id_cmc/maxID

# ------------------------------------------------------
# Print to console
print 'Hip Flexion Moment'
print 'rmsdiff=',rms_id_cmc[0]
print 'rmsdiff norm to peak ID=', rms_id_cmc_norm[0]
print 'peak diff=', peak_id_cmc[0]
print 'peak diff norm to peak ID=', peak_id_cmc_norm[0]
print ' '
print 'Knee Extension Moment'
print 'rmsdiff=',rms_id_cmc[1]
print 'rmsdiff norm to peak ID=', rms_id_cmc_norm[1]
print 'peak diff=', peak_id_cmc[1]
print 'peak diff norm to peak ID=', peak_id_cmc_norm[1]
print ' '
print 'Ankle Extension Moment'
print 'rmsdiff=',rms_id_cmc[2]
print 'rmsdiff norm to peak ID=', rms_id_cmc_norm[2]
print 'peak diff=', peak_id_cmc[2]
print 'peak diff norm to peak ID=', peak_id_cmc_norm[2]

plt.show()