import json
from string import Template
import os
from popen2 import popen2

cwd = os.path.dirname(os.path.abspath(__file__))
full_storage_dir = cwd + '/../storage'

if not os.path.exists(full_storage_dir):
  os.makedirs(full_storage_dir)

def main():
  submit_jobs()

def submit_jobs():
  with open(cwd + '/../jobs/metadata.json') as data_file:    
    data = json.load(data_file)

  jobs_dir = data['jobs_dir']

  for job_dir in jobs_dir:
    full_job_dir = cwd + '/../jobs/' + job_dir

    with open(full_job_dir + '/config.json') as config_file:
      config = json.load(config_file)

    default_args = config['default_inputs']
    name = config['name']
    resources = config['resources']
    inputs = config['inputs']
    resources['job_dir'] = full_job_dir
    resources['storage_dir'] = full_storage_dir
 
    job_template = Template("""
    #!/bin/bash
    #PBS -l nodes=$nodes:ppn=$ppn
    #PBS -l walltime=$walltime
    #PBS -q $queue
    #PBS -N $name
    #PBS -o $storage_dir/stdout
    #PBS -e $storage_dir/stderr

    module purge
    module load intel/14.0.2
    module load openmpi/1.8
    module load libxc/2.2.2
    module load mkl/11.2
    module load fftw/3.3.4
    module load python/2.7

    python $job_dir/../generalComputing.py $params >> $storage_dir/$name.out
    """).safe_substitute(resources)

    # submitting jobs based available input range
    for inp in inputs:
      # create params string
      s = ""
      run_sh = job_template
      for key in inp:
          s += "--{}={} ".format(key, inp[key])

      # use default arguments in not specified
      for key in default_args:
          if key not in inp:
            s += "--{}={} ".format(key, default_args[key])
      s += "--{}={}".format("name",name)
      run_sh = Template(run_sh).substitute(name=name, params=s)
      submit_helper(run_sh)

def submit_helper(run_sh):
    output, input = popen2('qsub')
    input.write(run_sh)
    input.close()
    return output.read()

if __name__ == "__main__":
    main()
