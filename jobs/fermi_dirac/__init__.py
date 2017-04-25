#!/usr/bin/python
import time as time
import sys, getopt
import numpy as np

def evaluate(args):
    epsilon = float(args['eps'][0])
    mu = float(args['mu'][0])
    T = float(args['t'][0])
    kB = 8.615e-5 #eV/K (we will typically use energy units of eV)
    n = 1.0 /(np.exp((epsilon - mu)/(kB * T)) + 1.0)
    return n
