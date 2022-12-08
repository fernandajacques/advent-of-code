
import re

def prismArea(l, w, h):

    side_a = l * w
    side_b = w * h
    side_c = h * l

    smallestSide = min([side_a, side_b, side_c])
    area = (2* side_a) + (2* side_b) + (2* side_c)
    total_paper = area + smallestSide

    return total_paper

#prismArea(2, 3, 4)
#prismArea(1, 1, 10)
total_wrapping_paper = 0
with open('Data_d02p01.txt', 'r') as mydata:
    for myline in mydata:
        num = [int(s) for s in re.findall(r'\d+', myline)]
        value = prismArea(num[0], num[1], num[2])
        total_wrapping_paper = total_wrapping_paper + value
    
    print(total_wrapping_paper)
