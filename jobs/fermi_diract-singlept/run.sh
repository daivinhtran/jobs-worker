#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:15:00
#PBS -q joe-test
#PBS -N optimizer
#PBS -o stdout
#PBS -e stderr

# cd $PBS_O_WORKDIR

module purge
module load intel/14.0.2
module load openmpi/1.8
module load libxc/2.2.2
module load mkl/11.2
module load fftw/3.3.4
module load python/2.7


python fermi_dirac-singlept.py #submit using mpirun (parallel computing) to 12 cores. The 12 here must match the ppn specified in the header.
