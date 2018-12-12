## OpenSim Full Body Model with Python

This project extends [**Full Body Model for use in Dynamic Simulations of Human Gait**](https://simtk.org/projects/full_body) with Python scripts which are equivalent to the Matlab scrips provided with the model.

This Python code was derived from the original Matlab code, and where possible the names of scripts, the comments, and the names of variables were preserved.

###Requirements
+ opensim installed and added to the Path
+ Python 2 installed
+ Python packages:
	+ os
	+ subprocess
	+ numpy
	+ scipy
	+ matplotlib
	+ pandas
	+ StringIO
	+ opensim
	
**Note:** All required Python dependencies (except for opensim) are included in the [Anaconda](https://www.anaconda.com/) platform.

	
###How to Use
Download the model from the repository (registration required):
https://simtk.org/projects/full_body
Extract files to a directory

Clone this project or download its zip and extract it.

Copy `Python` dir to the model's directory
Your directories should look like:

+ SimulationDataAndSetupFiles
	+ CMC
	+ ExpData
	+ Geometry
	+ ID
	+ IK
	+ Python
	+ RRA
	+ Scale
	+ scripts
	+ videos

Go to the Python dir and run scripts from there. Instructions are the same as for the original Matlab scripts.

**Note:** Two `.mat` files from the distribution were converted to tab-delimited text files: `emg_run.txt` and `emg_walk.txt`.



