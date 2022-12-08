counting1478 = 0

with open('DataDay08.txt', 'r') as mydata:
    for line in mydata:

        parts = line.split(' | ')
        signalPattern = parts[0].split(' ')
        outputValues = parts[1].strip("\n")
        outputValues = outputValues.split(' ')

        for item in outputValues:

            if len(item) == 2 or len(item) == 4 or len(item) == 3 or len(item) == 7:
                counting1478 +=1
            
            else:
                continue

print(f"Total of 1, 4, 7 and 8: {counting1478}")