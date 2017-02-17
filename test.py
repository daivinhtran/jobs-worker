#!/usr/bin/python

import sys, getopt

def main(argv):
   epsilon = None
   mu = None
   T = None
   try:
      opts, args = getopt.getopt(argv,"t:",["eps=", "mu="])
   except getopt.GetoptError:
      print 'test.py -t <T> -eps <epsilon> -mu <mu>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '--eps':
         epsilon = arg
      elif opt == '--mu':
         mu = arg
      elif opt == '-t':
         T = arg

   if epsilon is None or mu is None or T is None:
      print 'test.py -t <T> -eps <epsilon> -mu <mu>'
      sys.exit(2)

   

if __name__ == "__main__":
   main(sys.argv[1:])