
forwardList = []
depthList = []
aimList = []
depthMeasuments = 0
forwardCount = 0
aim = 0

with open('Data_d01p01.txt', 'r') as mydata:
    for line in mydata:
        newLine = line.rstrip("\n")
        newLine = newLine.split(' ')

        if newLine[0] == 'forward':
            forwardCount += int(newLine[1])
            forwardList.append(int(newLine[1]))
            depthMeasuments += (aim * int(newLine[1]))
        
        elif newLine[0] == 'down':
            aim += int(newLine[1])
            depthList.append(int(newLine[1]))
        
        elif newLine[0] == 'up':
            aim -= int(newLine[1])
            depthList.append(int(newLine[1]) * -1)
            
mydata.close()
print(depthMeasuments)
print(forwardCount)
print(depthList)
print(forwardList)
print(depthMeasuments * forwardCount)

