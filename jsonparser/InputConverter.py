# DEPRECATED FOR LATER USE

import json
import itertools

with open('inputs.json') as json_file:
    data = json.load(json_file)
    mode = data['mode']
    types = data['types']
    fieldNames = data['names']
    inputs = []

    # Obtaining inputs through different modes
    if mode == 'CartesianProduct':
        inputList = []
        for k, v in data['values'].items():
            inputList.append(v)
        for inputComb in itertools.product(*inputList):
            currentInput = []
            for element in range(len(inputComb)):
                typing = types[element]
                if typing == 'tuple':
                    currentInput.append(tuple(inputComb[element]))
                elif typing == 'set':
                    currentInput.append(set(inputComb[element]))
                elif typing == 'list':
                    currentInput.append(list(inputComb[element]))
                elif typing == 'dict':
                    currentInput.append(dict(inputComb[element]))
                else:
                    currentInput.append(inputComb[element])
            inputs.append(currentInput)
    elif mode == 'Manual':
        for value in data['values']:
            currentInput = []
            for name in fieldNames:
                typing = types[name]
                if typing == 'tuple':
                    currentInput.append(tuple(value[name]))
                elif typing == 'set':
                    currentInput.append(set(value[name]))
                elif typing == 'list':
                    currentInput.append(list(value[name]))
                elif typing == 'dict':
                    currentInput.append(dict(value[name]))
                else:
                    currentInput.append(value[name])
            inputs.append(currentInput)

    module = __import__(data['fileName'])
    function = getattr(module, data['functionName'])
    callback = getattr(module, data['callbackName'])
    for input in inputs:
        # Whatever needs to be done with output
        callback(function(*input))


