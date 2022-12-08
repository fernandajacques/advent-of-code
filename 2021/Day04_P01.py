
import re
import copy

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

def checkNumbers(numbers,card):
    
    winnerNumbers = []
    for n in numbers:
        
        for i in range(5):
            for j in range(5):

                if n == card[i][j]:
                    winnerNumbers.append(n)

    return winnerNumbers

cards = {}
myList = []

with open('DataDay04.txt', 'r') as mydata:
    text = mydata.read()

parts = text.split('\n\n')
drawNumbers = parts[0].split(',')

for n in range(1, len(parts)):
    mycards = parts[n].splitlines()
    myList.append(mycards)

for n in range(len(myList)):

    cardKey = 'card' + str(n)
    cardValues = []
    
    for i in range(5):
        valueList = re.findall('[0-9]+', myList[n][i])

        #print(valueList)
        cardValues.append(valueList)

    cards[cardKey] = cardValues

cardsCopy = copy.deepcopy(cards)
# print(f'cards : {cards}')
# print(f'cardsCopy : {cardsCopy}')

numbersDrawn = []
winner = False

for n in drawNumbers:

    numbersDrawn.append(n)

    for key in cards.keys():
        v = cards.get(key)
        win = bingo(numbersDrawn, v)

        if win == True:
            w = cardsCopy.get(key)
            winNums = checkNumbers(numbersDrawn, cardsCopy.get(key))

            sumOfCard = 0
                       
            for i in range(5):
                for j in range(5):

                    if v[i][j] != 1:
                        sumOfCard += int(v[i][j])

            print(f'Bingo result is {sumOfCard * int(numbersDrawn[-1])}')

            winner = True
            break
    
    if winner:
        break





