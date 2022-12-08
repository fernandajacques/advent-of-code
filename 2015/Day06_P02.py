
import numpy as np
import re
lightMatrix = np.zeros((1000,1000))

def state(data_line):

    #extract info: turn on, turn off or toggle
    light_state = data_line[0:7]
    if light_state == 'toggle ':
        return -1
    elif light_state == 'turn on':
        return 1
    elif light_state == 'turn of':
        return 0

with open('Data_d06p01.txt', 'r') as mydata:
    for input_line in mydata:
        num = [int(s) for s in re.findall(r'\d+', input_line)]
        lightState = state(input_line)

        for i in range(num[0], (num[2]+1)):
            for j in range(num[1], (num[3] +1)):

                if lightState == 1:
                    lightMatrix[i,j] += 1
                elif lightState == -1:
                    lightMatrix[i,j] += 2
                else:
                    lightMatrix[i,j] -=1
                    if lightMatrix[i,j] <0:
                        lightMatrix[i,j] = 0

totalBrightness = 0
for i in range(1000):
    for j in range(1000):
        totalBrightness = totalBrightness + lightMatrix[i,j]

print(totalBrightness)


