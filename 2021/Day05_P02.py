
import re
import numpy as np

def diagonals(mylist):

    m = (mylist[1]- mylist[3]) / (mylist[0]-mylist[2])
    b = mylist[1] - (m * mylist[0])

    return {'m': m, 'b': b}

ventGrid = np.zeros((1000,1000))

with open('DataDay05.txt', 'r') as mydata:
    for input_line in mydata:
        num = [int(s) for s in re.findall(r'\d+', input_line)]

        if num[0] == num[2] or num[1] == num[3]:

            if num[0] < num[2] or num[1] < num[3]:
                for i in range(num[0], (num[2]+1)):
                    for j in range(num[1], (num[3] +1)):

                        ventGrid[i,j] += 1

            elif num[0] > num[2] or num[1] > num[3]:
                for i in range(num[2], (num[0]+1)):
                    for j in range(num[3], (num[1] +1)):

                        ventGrid[i,j] += 1
            
        elif abs(num[0] - num[2]) == abs(num[1] - num[3]):

            linearEquation = diagonals(num)
            if num[0] < num[2]:
                for i in range(num[0], (num[2]+1)):
                    yPoints = int((linearEquation.get('m') *i) + linearEquation.get('b'))
                    ventGrid[i,yPoints] += 1

            elif num[0] > num[2]:
                for i in range(num[2], (num[0]+1)):

                    yPoints = int((linearEquation.get('m') *i) + linearEquation.get('b'))
                    ventGrid[i,yPoints] += 1


#print(ventGrid)
ventCount = 0

for i in range(1000):
    for j in range(1000):
            
        if ventGrid[i,j] > 1:
            ventCount +=1

print(ventCount)
