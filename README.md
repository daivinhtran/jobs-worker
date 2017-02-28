# Job Workers

## Introduction

Submit jobs to pbs system on PACE

## Install
* Simply log on to PACE
* ```$ module load git```
* ```$ git clone https://github.gatech.edu/vtran40/jobs-worker.git```
* ```$ module load python/2.7```
* ```$ virtualenv ENV```
* ```$ source ENV/bin/activate```
* ```$ cd jobs-worker```

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
│   │   ├── compute.py  
├── worker
│   ├── submit.py
├── storage (only in production)
│   ├── jobname.out
```

`jobs/metadata.json` specify what jobs the worker need to submit along with default resources 

```json
{
    "description": "this contains the folder name of the jobs that need to be submitted",
    "note": "please validate the file on jsonlint.com after each change",
    "jobs_dir":[
        "fermi_diract-singlept"
    ],
    "default_resources": {
        "nodes" : 4,
        "ppn": 1,
        "walltime": "00:15:00",
        "queue": "joe-test"
    }
}
```

Under each job directory (fermi-dirac-singlept, other-job, ...), `config.json` contains all the input range needed to complete the calculation written in ```compute.py```
```json
{
  "name": "fermi_dirac",
  "resources": {
    "nodes": 4,
    "ppn": 2,
    "walltime": "00:10:00",
    "queue": "joe-test"
  },
  "default_inputs": {
    "eps": 0.04,
    "mu": 1.0,
    "t": 400
  },
  "inputs": [
    {
      "eps": 0.01,
      "mu": 1.5,
      "t": 500
    },
    {
      "eps": 0.02
    }
  ]
}
```

`storage` folder is used to storage all the calculation after the jobs are completed. I've ignore the folder in development because we don't want to commit and push these data to version control.
## Usage guide
To submit all the jobs specified in jobs/metadata.json. Simple type this 1 command:
* ```$ python worker/submit.py```

All the computation will be stored under ```storage``` folder. Output from fermi_diract-singplept will be named as ```fermi_dirac.out``` because ```fermi_dirac``` is specified in the ```config.json``` for that job
