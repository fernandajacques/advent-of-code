
myList = []
depthMeasuments = {}

with open('Data_d01p01.txt', 'r') as mydata:
    for line in mydata:
        newLine = int(line.rstrip("\n"))
        myList.append(newLine)
mydata.close()

#print(myList)

indexCount = 0
for m in myList:

    while indexCount < len(myList)-3:
        value01 = myList[indexCount] + myList[indexCount+1] + myList[indexCount+2]
        value02 = myList[indexCount+1] + myList[indexCount+2] + myList[indexCount+3]
        anyName = str(myList[indexCount])+str(indexCount)
        #print(value01, value02)
        indexCount+=1

        if value01 < value02:
            depthMeasuments[anyName] = 1
        elif value01 > value02:
            depthMeasuments[anyName] = 0
        else:
            continue
    

#print(depthMeasuments)
#print(myList)

totalLarger = 0

for key in depthMeasuments:
    myValue = depthMeasuments.get(key)
    #print(myValue)
    if myValue == 1:
        totalLarger +=1

print(totalLarger)