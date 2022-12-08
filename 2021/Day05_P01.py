
import re
import numpy as np

ventGrid = np.zeros((10,10))

with open('mockdata.txt', 'r') as mydata:
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

ventCount = 0

for i in range(10):
    for j in range(10):
            
        if ventGrid[i,j] > 1:
            ventCount +=1

print(ventCount)
