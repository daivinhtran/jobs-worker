#!/bin/bash
#PBS -l nodes=1:ppn=16
#PBS -l walltime=12:00:00
#PBS -q joe-test
#PBS -N espresso_calculation
#PBS -o /nv/hp13/yzhang3027/jobs-worker/worker/../storage/stdout
#PBS -e /nv/hp13/yzhang3027/jobs-worker/worker/../storage/stderr

module purge
module load intel/14.0.2
module load openmpi/1.8
module load libxc/2.2.2
module load mkl/11.2
module load fftw/3.3.4
module load python/2.7
source /nv/hp22/amedford6/medford-shared/envs/espresso-5.1.r11289-pybeef
python /nv/hp13/yzhang3027/jobs-worker/worker/../jobs/espresso_calculation/../generalComputing.py --kpts=[8,@8,@1]@@--pw=400@@--parflags=-nk@2@@--beefensemble=True@@--printensemble=True@@--dw=4000@@--spinpol=False@@--outdir=esp_log@@--name=espresso_calculation >> /nv/hp13/yzhang3027/jobs-worker/worker/../storage/espresso_calculation.out
