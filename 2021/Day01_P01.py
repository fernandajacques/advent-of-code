
myList = []
depthMeasuments = {}

with open('Data_d01p01.txt', 'r') as mydata:
    for line in mydata:
        newLine = int(line.rstrip("\n"))
        myList.append(newLine)
mydata.close()

indexCount = 0
for m in myList:

    while indexCount < len(myList)-1:
        value01 = myList[indexCount]
        value02 = myList[indexCount+1]
        anyName = str(value02)+str(indexCount)
        #print(value01, value02)

        if value01 < value02:
            depthMeasuments[anyName] = 1
        elif value01 > value02:
            depthMeasuments[anyName] = 0
        else:
            continue
        indexCount+=1

#print(depthMeasuments)
#print(myList)

totalLarger = 0

for key in depthMeasuments:
    myValue = depthMeasuments.get(key)
    #print(myValue)
    if myValue == 1:
        totalLarger +=1

print(totalLarger)