def mostDigit(i, myList):

    counting1s = 0
    counting0s = 0

    for item in myList:

        if item[i] == '1':
            counting1s += 1

        elif item[i] == '0':
            counting0s += 1

    if counting0s > counting1s:
        return '0'
    elif counting0s < counting1s:
        return '1'
    else:
        return '1'

def leastDigit(i, myList):

    counting1s = 0
    counting0s = 0

    for item in myList:

        if item[i] == '1':
            counting1s += 1

        elif item[i] == '0':
            counting0s += 1

    if counting0s < counting1s:
        return '0'
    elif counting0s > counting1s:
        return '1'
    else:
        return '0'


def binaryFilter(ind,b,myList):

    resultList = []

    for item in myList:
        if b == item[ind]:
            resultList.append(item)
    
    return resultList

oxygen = [[]]
carbon = [[]]

with open('Data_d03p01.txt', 'r') as mydata:
    for line in mydata:
        line = line.rstrip("\n")
        oxygen[0].append(line)
        carbon[0].append(line)

mydata.close()

for n in range(len(oxygen[0][0])):

    if len(oxygen[-1]) > 1:

        binMostDigit = mostDigit(n, oxygen[n])
        filteredList = binaryFilter(n,binMostDigit,oxygen[n])
        oxygen.append(filteredList)
        #print(oxygen)

for n in range(len(carbon[0][0])):

    if len(carbon[-1]) > 1:

        binLeastDigit = leastDigit(n, carbon[n])
        filteredList = binaryFilter(n,binLeastDigit,carbon[n])
        carbon.append(filteredList)
        #print(carbon)

print(oxygen[-1])
print(carbon[-1])


oxygenRating = int(oxygen[-1][0], 2)
carbonRating = int(carbon[-1][0], 2)
print(f'Life support rating: {oxygenRating * carbonRating}')