
# Make walking simulations, and generate
#   (1) muscle-generated vs. inverse dynamics joint moments
#   (2) simulated muscle activity vs. emg
execfile('simulateWalk.py')
execfile('validationPlots_emg_walk.py')
execfile('validationPlots_id_walk.py')
execfile('validation_RRA_CMC_trackingErrors_walk.py')

# Make running simulations, and generate
#   (1) muscle-generated vs. inverse dynamics joint moments
#   (2) simulated muscle activity vs. emg
execfile('simulateRun.py')
execfile('validationPlots_emg_run.py')
execfile('validationPlots_id_run.py')
execfile('validation_RRA_CMC_trackingErrors_run.py')
