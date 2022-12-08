
import re
def initialList(ini_List):

    fishList = [0,0,0,0,0,0,0,0,0]

    for item in ini_List:
        if item == 0:
            fishList[0] +=1
        elif item == 1:
            fishList[1] +=1
        elif item == 2:
            fishList[2] +=1
        elif item == 3:
            fishList[3] +=1
        elif item == 4:
            fishList[4] +=1
        elif item == 5:
            fishList[5] +=1
        elif item == 6:
            fishList[6] +=1
        elif item == 7:
            fishList[7] +=1
        elif item == 8:
            fishList[8] +=1

    return fishList

def updatingSchool(mySchool):

    newSchool = []

    newSchool.append(mySchool[1])
    newSchool.append(mySchool[2])
    newSchool.append(mySchool[3])
    newSchool.append(mySchool[4])
    newSchool.append(mySchool[5])
    newSchool.append(mySchool[6])
    newSchool.append(mySchool[7]+ mySchool[0])
    newSchool.append(mySchool[8])
    newSchool.append(mySchool[0])
    
    return newSchool

with open('DataDay06.txt', 'r') as mydata:
    for input_line in mydata:
        initialSchool = [int(s) for s in re.findall(r'\d+', input_line)]
        school = initialList(initialSchool)

day = 256

for d in range(day):

    school = updatingSchool(school)

print(school)
total = 0

for item in school:
    total +=item
print(total)
