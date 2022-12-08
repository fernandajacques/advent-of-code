myList = []
forwardList = []
depthList = []
depthMeasuments = 0
forwardCount = 0

with open('Data_d01p01.txt', 'r') as mydata:
    for line in mydata:
        newLine = line.rstrip("\n")
        newLine = newLine.split(' ')
        myList.append(newLine)

        if newLine[0] == 'forward':
            forwardCount += int(newLine[1])
            forwardList.append(int(newLine[1]))
        
        elif newLine[0] == 'down':
            depthMeasuments += int(newLine[1])
            depthList.append(int(newLine[1]))
        
        elif newLine[0] == 'up':
            depthMeasuments -= int(newLine[1])
            depthList.append(int(newLine[1]) * -1)
            
mydata.close()
print(depthMeasuments)
print(forwardCount)
print(depthList)
print(forwardList)
print(depthMeasuments * forwardCount)

