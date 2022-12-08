
import re

def lanternfishSchool(myList):

    newList = []
    for item in myList:
        if item <9 and item > 0:
            newList.append(item-1)
        
        elif item == 0:
            newList.append(6)
            newList.append(8)

    return newList

school = []

with open('DataDay05.txt', 'r') as mydata:
    for input_line in mydata:
        initialSchool = [int(s) for s in re.findall(r'\d+', input_line)]
        school.append(initialSchool)

days = 80
dayCount = 0

for day in range(days):
    lanternfish = lanternfishSchool(school[day])
    school.append(lanternfish)
    dayCount +=1


print(len(school[-1]))


