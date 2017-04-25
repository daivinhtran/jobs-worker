#!/usr/bin/python

import sys
import os
import json
import itertools

def isInteger(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def isFloat(i):
    try:
        float(i)
        return True
    except ValueError:
        return False


def main():
    if len(sys.argv) < 2:
        sys.exit("Input file location not specified.")
    inputFile = open(sys.argv[1], 'r')

    # Parsing for Location of config.json
    outputDirectory = inputFile.readline().rstrip()
    outputs = [x.strip() for x in outputDirectory.split('|')]
    outputDirectory = outputs[1]
    outputDirectory = os.path.join(outputDirectory, "config.json")

    # Specify Job Name
    jobName = [x.strip() for x in inputFile.readline().rstrip().split('|')][1]

    # Specify Number of Nodes
    nodes = int([x.strip() for x in inputFile.readline().rstrip().split('|')][1])

    # Specify PPN
    ppn = int([x.strip() for x in inputFile.readline().rstrip().split('|')][1])

    # Specify Walltime
    walltime = [x.strip() for x in inputFile.readline().rstrip().split('|')][1]

    # Specify Queue
    queue = [x.strip() for x in inputFile.readline().rstrip().split('|')][1]

    # Accepting Input Ranges
    defaultInputs = {}
    otherInputRanges = {}
    for line in inputFile:
        lineSplit = [x.strip() for x in line.rstrip().split('|')]
        if len(lineSplit) < 3:
            if isInteger(lineSplit[1]):
                defaultInputs[lineSplit[0]] = int(lineSplit[1])
            elif isFloat(lineSplit[1]):
                defaultInputs[lineSplit[0]] = float(lineSplit[1])
            else:
                defaultInputs[lineSplit[0]] = lineSplit[1]
        else:
            inputName = lineSplit[0]
            lineSplit = lineSplit[1:]
            inputRange = []
            for section in lineSplit:
                section = section.strip()
                if section.startswith('(') or section.startswith('[') or section.startswith('<') or section.startswith('{'):
                    # Nested
                    section = section[1:-1]
                splits = [x.strip() for x in section.rstrip().split(',')]
                nested = []
                for i in splits:
                    if isInteger(i):
                        nested.append(int(i))
                    elif isFloat(i):
                        nested.append(float(i))
                    else:
                        nested.append(i)
                inputRange.append(nested)
            otherInputRanges[inputName] = inputRange

    # Freeing Resources
    inputFile.close()

    # Taking Cartesian Product to Generate Inputs
    inputList = [dict(itertools.izip(otherInputRanges, x)) for x in itertools.product(*otherInputRanges.itervalues())]

    for combination in inputList:
        for key, value in combination.iteritems():
            if len(value) == 1:
                combination[key] = value[0]

    # Writing config.json
    data = {}
    data['inputs'] = inputList
    data['default_inputs'] = defaultInputs
    data['resources'] = {'nodes' : nodes, 'ppn' : ppn, 'walltime' : walltime, 'queue' : queue}
    data['name'] = jobName

    # Writing to JSON file
    with open(outputDirectory, 'w') as outfile:
        json.dump(data, outfile, indent=4)



if __name__ == "__main__":
    main()