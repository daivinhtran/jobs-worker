#This is a heavy calculation that requires the use of a supercomputer. It must be submitted using the run.sh script.

#Import all necessary modules
from ase import io
from ase.parallel import paropen as open #ensures that open works in parallel environment
from ase.optimize import QuasiNewton #geometry optimization algorithm; QuasiNewton links to BFGS line search, which is the best general-purpose optimizer, but other options are available: https://wiki.fysik.dtu.dk/ase/ase/optimize.html
from espresso import espresso

#setup calculator

calcargs = dict(xc='BEEF-vdW',
        beefensemble=True,
        printensemble=True,
        kpts=(8, 8, 1), #only need 1 kpt in z-direction
        pw=400.,
        dw=4000.,
        spinpol=False,
        parflags='-nk 2',
        outdir ='esp_log')

calc = espresso(**calcargs)

atoms = io.read('Pt_111.json') #Read in the structure built by the other script

atoms.set_calculator(calc)

energy = atoms.get_potential_energy() #this is the potential energy of the electrons as computed by DFT. It will be closely related to the enthalpy.

f = open('converged.log','w')
f.write(str(energy))
f.close()
#This is not technically necessary, but it is often helpful to have a file that confirms whether or not a simulation has converged.
#Now we know that if 'converged.log' exists then the calculation has finished without having to check the queue.
