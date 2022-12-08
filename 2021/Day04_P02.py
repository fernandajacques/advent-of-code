
import re

def bingo(numbers, card):

    win = False
    for n in numbers:
        
        for i in range(5):
            for j in range(5):

                if n == card[i][j]:
                    card[i][j] = 1

    for ii in range(5):
        count = 0
        for jj in range(5):
            if card[ii][jj] == 1:
                count += 1
            if count == 5:
                win = True
                break
            
    for jj in range(5):
        count = 0
        for ii in range(5):
            if card[ii][jj] == 1:
                count += 1
            if count == 5:
                win = True
                break

    return win

cards = {}
myList = []

with open('DataDay04.txt', 'r') as mydata:
    text = mydata.read()

parts = text.split('\n\n')
drawNumbers = parts[0].split(',')

for n in range(1, len(parts)):
    mycards = parts[n].splitlines()
    myList.append(mycards)

leftOverCards = []

for n in range(len(myList)):

    cardKey = 'card' + str(n)
    leftOverCards.append(cardKey)
    cardValues = []
    
    for i in range(5):
        valueList = re.findall('[0-9]+', myList[n][i])

        cardValues.append(valueList)

    cards[cardKey] = cardValues

numOfCards = len(cards.keys())
numbersDrawn = []
lastWinner = []
check = True

for n in drawNumbers:

    numbersDrawn.append(n)
    for key in cards.keys():
        v = cards.get(key)

        if len(lastWinner) < numOfCards:

            win = bingo(numbersDrawn, v)

            if win == True:

                if key not in lastWinner:
                    lastWinner.append(key)
                    #print(lastWinner[-1])
        else:
            check = False
            break
        
    if check == False:
        break
        
w = cards.get(lastWinner[-1])
sumOfCard = 0
                       
for i in range(5):
    for j in range(5):

        if w[i][j] != 1:
            sumOfCard += int(w[i][j])

print(f'Bingo result is {sumOfCard * int(numbersDrawn[-1])}')

