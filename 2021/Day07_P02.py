
# Note for future-self: re-write this with 'soma dos termos de uma PA' to try and improve the speed.

import re
def fuel(mylist, position):

    fuel = []
    fuelTotal = 0

    for item in mylist:

        if item >= position:
            v = item - position
        
        else:
            v = position - item

        fuelValue = 0

        for n in range(v+1):
            fuelValue += n

        fuel.append(fuelValue)

    for f in fuel:
        fuelTotal += f

    return fuelTotal


with open('DataDay07.txt', 'r') as mydata:
    for input_line in mydata:
        crabPositions = [int(s) for s in re.findall(r'\d+', input_line)]

maxdata = max(crabPositions)
fuelConsumption = []

for n in range(maxdata+1):
    fuelValue = fuel(crabPositions,n)
    fuelConsumption.append(fuelValue)

minConsumption = min(fuelConsumption)

print(f"Least fuel possible {minConsumption}")

