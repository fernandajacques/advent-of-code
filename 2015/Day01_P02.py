
the_file = open('Data_d01p01.txt', 'r')
data = the_file.read()
the_file.close()

#data = "()())"
#data = ')'

floor = 0
char = 0
cond = True

while cond:
    for sym in data:
        if sym == "(":
            floor +=1
        elif sym == ")":
            floor -=1

        char += 1
        if floor == -1:
            print(char)
            cond = False
            break
            
    cond = False
