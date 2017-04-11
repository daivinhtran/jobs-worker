import time as time
import sys, getopt
import numpy as np
#import importlib

class DynamicImporter:
     def __init__(self, module_name):
         self.module = __import__(module_name)
def main(argv):
    t = time.strftime("%H:%M:%S__%m-%d-%Y")
    output = str(t)
    for key in argv:
        if(key!='name'):
            output+=", "+str(key)+"="+str(argv[key][0])
    funcName = argv[key][0]
    #i = importlib.import_module(funcName+".compute")
    dynamicImporter = DynamicImporter(funcName)
    i =dynamicImporter.module
    output+=", "+"Result="+str(i.evaluate(argv))
    print(output)
#def parseSysParam(argv):
    #from collections import defaultdict
   # d=defaultdict(list)
  #  for k, v in ((k.lstrip('-'), v) for k,v in (a.split('=') for a in argv)):
 #       d[k].append(v)
#    return dict(d)
def parseSysParam(argv):
    argList = argv[0].split("@@")
    from collections import defaultdict
    d = defaultdict(list)
    for ele in argList:
	ele = ele.replace("@"," ")
	partitions = ele.split('=')
	d[partitions[0].lstrip('-')].append(partitions[1])
    return dict(d)
if __name__ == "__main__":
    args = parseSysParam(sys.argv[1:])
    main(args)
 
