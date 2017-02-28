
#!/usr/bin/python
import time as time
import sys, getopt
import numpy as np
import pylab as plt

def main(argv):
    epsilon = None
    mu = None
    T = None
    try:
      opts, args = getopt.getopt(argv,"",["eps=", "mu=", "t="])
    except getopt.GetoptError:
      print 'compute.py -t <T> -eps <epsilon> -mu <mu>'
      sys.exit(2)

    for opt, arg in opts:
      if opt == '--eps':
        epsilon = float(arg)
      elif opt == '--mu':
        mu = arg = float(arg)
      elif opt == '--t':
        T = arg = int(arg)

    if epsilon is None or mu is None or T is None:
      print 'compute.py -t <T> -eps <epsilon> -mu <mu>'
      sys.exit(2)
    t = time.strftime("%H:%M:%S__%m-%d-%Y")
    print(str(t)+", "+str(epsilon)+", "+str(mu)+", "+str(T)+", "+str(fermi_dirac(epsilon, mu, T))+"\n")

def fermi_dirac(epsilon, mu, T):
    kB = 8.615e-5 #eV/K (we will typically use energy units of eV)
    n = 1.0/(np.exp((epsilon-mu)/(kB*T)) + 1.0)
    return n

if __name__ == "__main__":
    main(sys.argv[1:])
 
