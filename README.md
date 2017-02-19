# Job Workers

## Usage:

Submit jobs to pbs system on PACE

## Installation:
* Simply log on to PACE
* ```$ module load git```
* ```$ git clone https://github.gatech.edu/vtran40/jobs-worker.git```
* ```$ module load python/2.7```
* ```$ virtualenv ENV```
* ```$ source ENV/bin/activate```
* ```$ cd jobs-worker```
* ```$ pythnon worker/submit.py```
## Files
Directory structure:
```
├── README.md
├── jobs
│   ├── medadata.json
│   ├── fermi-dirac-singlept
│   │   ├── config.json
│   │   ├── compute.py
│   ├── other-job
│   │   ├── config.json
│   │   ├── compute.json  
├── worker
│   │   ├── submit.py
├── storage (only in production)
│   ├── jobname.out
```

`jobs/metadata.json` specify what jobs the worker need to submit along with default resources 

Under each job directory (fermi-dirac-singlept, other-job, ...), `config.json` contains all the input range needed to complete the calculation written in ```compute.py```

`storage` folder is used to storage all the calculation after the jobs are completed. I've ignore the folder in development because we don't want to commit and push these data to version control.
