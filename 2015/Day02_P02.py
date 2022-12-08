
import re

def ribbon(l, w, h):

    measures = [l,w,h]
    bow = l*w*h
    measures.pop(measures.index(max(measures)))
    ribbon_length = (2* measures[0]) + (2*measures[1])

    total_ribbon = ribbon_length + bow

    return total_ribbon

total_rib = 0
with open('Data_d02p01.txt', 'r') as mydata:
    for myline in mydata:
        num = [int(s) for s in re.findall(r'\d+', myline)]
        value = ribbon(num[0], num[1], num[2])
        total_rib = total_rib + value
    
    print(total_rib)
