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
|   ├── generalComputing.py
│   ├── fermi-dirac-singlept
│   │   ├── config.json
│   │   ├── compute.py
│   ├── other-job
│   │   ├── config.json
│   │   ├── compute.py  
|   |   ├── other needed files
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

`storage` folder is used to store all the calculations after the jobs have completed. The folder is ignored in this development because we don't yet want to commit and push these data to version control.

## Generating Inputs
Our system works well for small numbers of jobs, but often times, it's desireable to generate the input combinations from a range of inputs, a Direct Product. For example, let's say I want the range `input1 = [1, 2]` and range `input2 = [5, 6]`. While it's certainly possible to do this manually for our system, to specify each combination of inputs of the Direct Product `(1, 5), (1, 6), (2, 5), (2, 6)`, it does not generalize well for larger inputs.

So, we have created an input generator to generate the `config.json` file given a range of values. To do this, we need an input file like `inputs.txt` below.
```
config_file_directory_out | ../jobs/espresso_calculation
job_name | espresso_calculation
nodes | 1
ppn | 16
walltime | 00:10:00
queue | joe-test
beefensemble | True
printensemble | True
dw | 4000
spinpol | False
parflags | -nk 2
outdir | esp_log
kpts | (4, 4, 1) | (6, 6, 1) | (8, 8, 1) | (10, 10, 1) | (12, 12, 1) | (16, 16, 1)
pw | 300 | 400 | 500 | 600 | 800 | 1000
```
In the above file, the `|` symbol is used as a delimeter between inputs. The fields `config_file_directory_out` to `queue` are mandatory and should be in that order. Everything afterwards specifies the name of the field followed by the input values for the direct product.

To use this functionality, use the python command:
* ```$ python /path/to/jsonparser/JSONGenerator.py /path/to/and/name/of/inputs.txt```
where you fill in the appropriate paths.

Currently, this direct product inputs generator only works for standard python types such as ints, floats, lists, tuples, sets, etc. It also doesn't work for deeply nested python data structures. We hope to, in the future, add functionality for Object-Oriented python input generation.

## Usage guide
To submit all the jobs specified in jobs/metadata.json. Simply type this 1 command:
* ```$ python worker/submit.py```

All the computation will be stored under ```storage``` folder. Output from fermi_diract-singplept will be named as ```fermi_dirac.out``` because ```fermi_dirac``` is specified in the ```config.json``` for that job
