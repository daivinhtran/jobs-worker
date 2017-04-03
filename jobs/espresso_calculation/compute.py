#!/usr/bin/python
import time as time
import sys, getopt
import numpy as np
import pylab as plt
from ase import io
from ase.parallel import paropen as open #ensures that open works in parallel environment
from ase.optimize import QuasiNewton #geometry optimization algorithm; QuasiNewton links to BFGS line search, which is the best general-purpose optimizer, but other options are available: https://wiki.fysik.dtu.dk/ase/ase/optimize.html
from espresso import espresso

def evaluate(args):
	x = str(args['xc'][0])
	be = bool(str(args['beefensemble'][0]))
	pe = bool(str(args['printensemble'][0]))
	kpoints = tuple(float(args['kpts'][0][0]), float(args['kpts'][0][1]), float(args['kpts'][0][2]))
	p = float(args['pw'][0])
	d = float(args['dw'][0])
	sp = bool(args['spinpol'][0])
	pflags = str(args['parflags'][0])
	odir = str(args['outdir'][0])
	
	calcargs = dict(xc = x,
    	beefensemble = be,
    	printensemble = pe,
    	kpts = kpoints, #only need 1 kpt in z-direction
    	pw = p,
    	dw = d,
    	spinpol = sp,
    	parflags = pflags,
    	outdir = odir)

	calc = espresso(**calcargs)
	
	atoms = io.read('Pt_111.json') #Read in the structure built by the other script

	atoms.set_calculator(calc)

	energy = atoms.get_potential_energy() #this is the potential energy of the electrons as computed by DFT. It will be closely related to the enthalpy.

	f = open('converged.log','w')
	f.write(str(energy))
	f.close()

	return calc
