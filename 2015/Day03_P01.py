
# move01 = '^'
# moves02 = '^>v<'
# moves03 = '^v^v^v^v^v'

the_file = open('Data_d03p01.txt', 'r')
my_list = the_file.read()
the_file.close()


position= [[0,0]]
count = 0

def current_position(position, move):

    new_position = list(position)

    if move == '>':
        new_position[0] +=1
    elif move == '<':
        new_position[0] -=1
    elif move == '^':
        new_position[1] +=1
    elif move == 'v':
        new_position[1] -=1

    return new_position

for m in my_list:
    new_position = current_position(position[count], m)
    position.append(new_position)
    count +=1

#print(position)

unique_list = []
     
for x in position:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)
print(len(unique_list))