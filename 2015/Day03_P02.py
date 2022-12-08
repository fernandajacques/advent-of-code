
#Santa delivering presents taking turns with Robo Santa
# moves01 = '^v'
# moves02 = '^>v<'
# moves03 = '^v^v^v^v^v'

the_file = open('Data_d03p01.txt', 'r')
my_list = the_file.read()
the_file.close()


position_santa= [[0,0]]
position_robo = [[0,0]]
count_santa = 0
count_robo = 0

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

count_index = 1

for m in my_list:

    if (count_index %2) == 0:
        new_position = current_position(position_robo[count_robo], m)
        position_robo.append(new_position)
        count_robo +=1
        count_index += 1
    
    else:
        new_position = current_position(position_santa[count_santa], m)
        position_santa.append(new_position)
        count_santa +=1
        count_index += 1

all_positions = position_robo + position_santa

unique_list = []
     
for x in all_positions:
    if x not in unique_list:
        unique_list.append(x)

#print(unique_list)
print(len(unique_list))