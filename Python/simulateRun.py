import os
import opensim as osim

from simFunctions import runProgram, \
                         getField, \
                         setMassOfBodiesUsingRRAMassChange, \
                         scaleOptimalForceSubjectSpecific, \
                         setMaxContractionVelocityAllMuscles

# Base dir
# assume we are running from baseDir/Python
curPath = os.getcwd()
[baseDir,sub]=os.path.split(curPath)
#print baseDir

# Scale 
os.chdir(baseDir + '/Scale')

cmdprog = 'opensim-cmd'
cmdtool = 'run-tool'
cmdfile = 'scale_setup_run_scaleOnly.xml'
cmdfull = [cmdprog, cmdtool, cmdfile]
rc = runProgram(cmdfull)

cmdfile = 'scale_setup_run.xml'
cmdfull = [cmdprog, cmdtool, cmdfile]
rc = runProgram(cmdfull)
    
# Inverse Kinematics
os.chdir(baseDir + '/IK')
cmdfile = 'ik_setup_run.xml'
cmdfull = [cmdprog, cmdtool, cmdfile]
rc = runProgram(cmdfull)
    
# RRA 1 
os.chdir(baseDir + '/RRA/run')
cmdfile = 'rra_setup_run_1.xml'
cmdfull = [cmdprog, cmdtool, cmdfile]
rc = runProgram(cmdfull)

with open('out.log', 'r') as flog:
  txtLog = flog.read()
  flog.close()

massChange = float(getField(txtLog, 'Total mass change: '))
print 'run, rra 1, dMass = ', massChange
dCOM = getField(txtLog, 'Mass Center (COM) adjustment: ')
print 'run, rra 1, dCOM = ', dCOM

osimModel_rraMassChanges = osim.Model('subject_run_rra1.osim')
osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel_rraMassChanges, massChange)
osimModel_rraMassChanges.printToXML('subject_run_rra1.osim')

# RRA 2 
cmdfile = 'rra_setup_run_2.xml'
cmdfull = [cmdprog, cmdtool, cmdfile]
rc = runProgram(cmdfull)

with open('out.log', 'r') as flog:
  txtLog = flog.read()
  flog.close()

massChange = float(getField(txtLog, 'Total mass change: '))
print 'run, rra 2, dMass = ', massChange
dCOM = getField(txtLog, 'Mass Center (COM) adjustment: ')
print 'run, rra 2, dCOM = ', dCOM

osimModel_rraMassChanges = osim.Model('subject_run_rra2.osim')
osimModel_rraMassChanges = setMassOfBodiesUsingRRAMassChange(osimModel_rraMassChanges, massChange)
osimModel_rraMassChanges.printToXML('subject_run_rra2.osim')


# Scale muscle forces based on final mass, set vmax
osimModel_postRRA = scaleOptimalForceSubjectSpecific(osimModel_rraMassChanges, osimModel_rraMassChanges, 1.70, 1.83)
osimModel_postRRA = setMaxContractionVelocityAllMuscles(osimModel_postRRA, 15.0)
osimModel_postRRA.printToXML(baseDir +'/CMC/run/subject_run_adjusted.osim');

# CMC
os.chdir(baseDir + '/CMC/run')
cmdfile = 'cmc_setup_run.xml'
cmdfull = [cmdprog, cmdtool, cmdfile]
rc = runProgram(cmdfull)

# ID
os.chdir(baseDir + '/ID')
cmdfile = 'id_setup_run.xml'
cmdfull = [cmdprog, cmdtool, cmdfile]
rc = runProgram(cmdfull)

os.chdir(baseDir + '/Python')
