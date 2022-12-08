

the_file = open('Data_d01p01.txt', 'r')
data = the_file.read()
the_file.close()

print(type(data))

#i = (")())())")
floor = 0

for sym in data:
    if sym == "(":
        floor +=1
    elif sym == ")":
       floor -=1

print(floor)
