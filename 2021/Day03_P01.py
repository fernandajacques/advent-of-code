
def eachDigit(i):

    counting1s = 0
    counting0s = 0
    with open('Data_d03p01.txt', 'r') as mydata:
        for line in mydata:

            if line[i] == '1':
            
                counting1s += 1
            elif line[i] == '0':
                counting0s += 1
         
    mydata.close()
    return {'z': counting0s, 'o': counting1s}

with open('Data_d03p01.txt', 'r') as mydata:
    first_line = mydata.readline()

mostCommon = []
leastCommon = []

for n in range(len(first_line)-1):
    #print(f'n {n}')
    binDigit = eachDigit(n)
    zeros = binDigit.get('z')
    ones = binDigit.get('o')
    #print(f'ones {ones}')
    #print(f'zeros {zeros}')

    if ones > zeros:
        mostCommon.append('1')
        leastCommon.append('0')
    else:
        mostCommon.append('0')
        leastCommon.append('1')

print(mostCommon)
print(leastCommon)

most = ''.join(mostCommon)
least = ''.join(leastCommon)

gamma = int(most, 2)
#print(type(most))
epsilon = int(least, 2)
print(f'Power consumption: {gamma * epsilon}')