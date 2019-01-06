from readSto import readStoFile
from simFunctions import matRMS
import numpy as np 

# Track max translational and rotational positional errors 
# from IK -> RRA kinematics, and RRA -> CMC kinematics

# subsets of coordinates
pelvis_trans = ['pelvis_tx', 'pelvis_ty', 'pelvis_tz']
pelvis_rot = ['pelvis_tilt', 'pelvis_list', 'pelvis_rotation']
lumbar = ['lumbar_extension', 'lumbar_bending', 'lumbar_rotation']
le = ['hip_flexion_r', 'hip_adduction_r', 'hip_rotation_r', 'knee_angle_r', 'ankle_angle_r',
      'hip_flexion_l', 'hip_adduction_l', 'hip_rotation_l', 'knee_angle_l', 'ankle_angle_l']
ue = ['arm_flex_r', 'arm_add_r', 'arm_rot_r', 'elbow_flex_r', 'pro_sup_r', 
      'arm_flex_l', 'arm_add_l', 'arm_rot_l', 'elbow_flex_l', 'pro_sup_l']

# load ik/rra kinematic errors
rra_results_dir = '../RRA/run/results_rra_2';
rra_run_pErr = readStoFile( rra_results_dir + '/rra_run_2_pErr.sto')
#for n in rra_run_pErr.columns : print n

rra_run_pErr_pelvisTrans = rra_run_pErr[pelvis_trans].values
rra_run_pErr_pelvisRot = rra_run_pErr[pelvis_rot].values
rra_run_pErr_lumbarRot = rra_run_pErr[lumbar].values
rra_run_pErr_leRot = rra_run_pErr[le].values
rra_run_pErr_ueRot = rra_run_pErr[ue].values

# print to console
print ; print 
print 'runing ik/rra errors'
print 'max rms pelvis error'
print '   ', 100*np.amax(matRMS(rra_run_pErr_pelvisTrans)), ' (trans, cm)'
print '   ', 100*np.amax(matRMS(rra_run_pErr_pelvisRot)), ' (rot, deg)'
print 'max rms lumbar error'
print '   ', 100*np.amax(matRMS(rra_run_pErr_lumbarRot)), ' (deg)'
print 'max rms LE error'
print '   ', 100*np.amax(matRMS(rra_run_pErr_leRot)), ' (deg)'
print 'max rms UE error'
print '   ', 100*np.amax(matRMS(rra_run_pErr_ueRot)), ' (deg)'
print ' '

print 'max pelvis error'
print '   ', 100*np.amax(np.abs(rra_run_pErr_pelvisTrans)), ' (trans, cm)'
print '   ', 180/np.pi*np.amax(np.abs(rra_run_pErr_pelvisRot)), ' (rot, deg)'
print 'max lumbar error'
print '   ', 180/np.pi*np.amax(np.abs(rra_run_pErr_lumbarRot)), ' (rot, deg)'
print 'max LE error'
print '   ', 180/np.pi*np.amax(np.abs(rra_run_pErr_leRot)), ' (rot, deg)'
print 'max UE error'
print '   ', 180/np.pi*np.amax(np.abs(rra_run_pErr_ueRot)), ' (rot, deg)'
print ' '

# load rra/cmc kinematic errors
cmc_results_dir = '../CMC/run/results'
cmc_run_pErr = readStoFile(cmc_results_dir + '/cmc_pErr.sto')
cmc_run_pErr_pelvisTrans = cmc_run_pErr[pelvis_trans].values
cmc_run_pErr_pelvisRot = cmc_run_pErr[pelvis_rot].values
cmc_run_pErr_lumbarRot = cmc_run_pErr[lumbar].values
cmc_run_pErr_leRot = cmc_run_pErr[le].values
cmc_run_pErr_ueRot = cmc_run_pErr[ue].values

# print to console
print 'runing rra/cmc errors'
print 'max rms pelvis error'
print '   ', 100*np.amax(matRMS(cmc_run_pErr_pelvisTrans)), ' (trans, cm)'
print '   ', 100*np.amax(matRMS(cmc_run_pErr_pelvisRot)), ' (rot, deg)'
print 'max rms lumbar error'
print '   ', 100*np.amax(matRMS(cmc_run_pErr_lumbarRot)), ' (deg)'
print 'max rms LE error'
print '   ', 100*np.amax(matRMS(cmc_run_pErr_leRot)), ' (deg)'
print 'max rms UE error'
print '   ', 100*np.amax(matRMS(cmc_run_pErr_ueRot)), ' (deg)'
print ' '

print 'max pelvis error'
print '   ', 100*np.amax(np.abs(cmc_run_pErr_pelvisTrans)), ' (trans, cm)'
print '   ', 180/np.pi*np.amax(np.abs(cmc_run_pErr_pelvisRot)), ' (rot, deg)'
print 'max lumbar error'
print '   ', 180/np.pi*np.amax(np.abs(cmc_run_pErr_lumbarRot)), ' (rot, deg)'
print 'max LE error'
print '   ', 180/np.pi*np.amax(np.abs(cmc_run_pErr_leRot)), ' (rot, deg)'
print 'max UE error'
print '   ', 180/np.pi*np.amax(np.abs(cmc_run_pErr_ueRot)), ' (rot, deg)'
print ' '

