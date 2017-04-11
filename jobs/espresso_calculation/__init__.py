import time as time
import sys, getopt
import numpy as np
from ase import io
from ase.parallel import paropen as open #ensures that open works in parallel environment
from ase.optimize import QuasiNewton #geometry optimization algorithm; QuasiNewton links to BFGS line search, which is the best general-purpose optimizer, but other options are available: https://wiki.fysik.dtu.dk/ase/ase/optimize.html
from espresso import espresso
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
def evaluate(args):
        x = 'BEEF-vdW'
        be = bool(str(args['beefensemble'][0]))
        pe = bool(str(args['printensemble'][0]))
        kpoints = (float(args['kpts'][0][1]), float(args['kpts'][0][4]), float(args['kpts'][0][7]))
        p = float(args['pw'][0])
        d = float(args['dw'][0])
        sp = bool(args['spinpol'][0])
        pflags = str(args['parflags'][0])
        odir = dir_path+"/"+str(args['outdir'][0])
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

        atoms = io.read(dir_path+'/Pt_111.json') #Read in the structure built by the other script

        atoms.set_calculator(calc)

        energy = atoms.get_potential_energy() #this is the potential energy of the electrons as computed by DFT. It will be closely related to the enthalpy.
        return energy

