from ase.build import molecule
from ase.visualize import view #this allows us to quickly view atomic structures from within the script using ASE's lightweight GUI.

#This script does not require a supercomputer, and should run from the login node (the node you first "land" on in a supercomputer) or from a desktop/laptop assuming you have python and the ASE python package installed.

#create the CO molecule using ASE's built in database of simple molecular structures
gas = molecule('CO')

gas.center(vacuum=5) #place the CO molecule in a box of vacuum with 5 Angstrom on each side

gas.write('CO.json') #we can write the atoms object to a .json file and then view it from the command line with "ase-gui" or load it into another script.

#It is generally better to think of the process of creating the atomic model as a separate step from actually calculating on it. This will make it easier to define arbitrarily complex atomic models, to transfer models between calculators, and to restart calculations.
