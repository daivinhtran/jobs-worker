
#!/usr/bin/python
import time as time
import sys, getopt
import numpy as np
import pylab as plt

def main(argv):
    t = time.strftime("%H:%M:%S__%m-%d-%Y")
    output = str(t)
    for key in argv:
        if(key!='name'):
            output+=", "+str(argv[key][0])
    output+=", "+str(fermi_dirac(argv))
    print(output)

def parseSysParam(argv):
    from collections import defaultdict
    d=defaultdict(list)
    for k, v in ((k.lstrip('-'), v) for k,v in (a.split('=') for a in argv)):
        d[k].append(v)
    return dict(d)

def fermi_dirac(args):
    epsilon = float(args['eps'][0])
    mu = float(args['mu'][0])
    T = float(args['t'][0])
    kB = 8.615e-5 #eV/K (we will typically use energy units of eV)
    n = 1.0 /(np.exp((epsilon - mu)/(kB * T)) + 1.0)
    return n

if __name__ == "__main__":
    args = parseSysParam(sys.argv[1:])
   
    main(args)
 
