import re
def fuel(mylist, position):

    fuel = []
    fuelTotal = 0

    for item in mylist:

        if item >= position:
            newValue = item - position
        
        else:
            newValue = position - item

        fuel.append(newValue)
    

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
