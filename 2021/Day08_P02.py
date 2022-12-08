def newWires(digits,output):

    digitDict = {}

    for d in digits:

        if len(d) ==2:
            digitDict[d] = 1
            digit1 = d

        elif len(d) == 3:
            digitDict[d] = 7
            digit7 = d
            #wireA = digit7[0]

        elif len(d) == 4:
            digitDict[d] = 4
            #digit4 = d

        elif len(d) == 7:
            digitDict[d] = 8
            digit8 = d

    for d in digits:

        if len(d) == 6:
            if digit1[0] not in d or digit1[1] not in d:
                digitDict[d] = 6
                digit6 = d

    for wire in digit8:
        if wire not in digit6:
            wireC = wire

    for d in digits:

        if len(d) == 5:
            if wireC not in d:
                digitDict[d] = 5
                digit5 = d

    for wire in digit6:
        if wire not in digit5:
            wireE = wire

    for wire in digit1:
        if wire != wireC:
            wireF = wire

    for d in digits:
        if wireF not in d:
            digitDict[d] = 2

        elif len(d) == 6:
            if wireE not in d:
                digitDict[d] = 9

    for d in digits:
        if len(d) ==5:
            if wireC in d and wireF in d:
                digitDict[d] = 3

        elif len(d) ==6:
            if wireC in d and wireE in d:
                digitDict[d] = 0

    decodedOutput =''

    for item in output:
        
        for k in digitDict.keys():
            if len(item) == len(k):

                if set(item).issubset(set(k)):
                    decodedOutput = decodedOutput + str(digitDict.get(k))

    outputValue = int(decodedOutput)
    return outputValue

sumOutput = 0

with open('DataDay08.txt', 'r') as mydata:
    for line in mydata:

        parts = line.split(' | ')
        signalPattern = parts[0].split(' ')
        outputValues = parts[1].strip("\n")
        outputValues = outputValues.split(' ')

        outp = newWires(signalPattern,outputValues)
        sumOutput += outp

print(f"This is the add up value: {sumOutput}")
