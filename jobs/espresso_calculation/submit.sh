#!/bin/bash
#PBS -l nodes=1:ppn=16
#PBS -l walltime=12:00:00
#PBS -q joe-6-intel
#PBS -N optimizer
#PBS -o stdout
#PBS -e stderr
cd $PBS_O_WORKDIR

source /nv/hp22/amedford6/medford-shared/envs/espresso-5.1.r11289-pybeef

python qn_opt.py 