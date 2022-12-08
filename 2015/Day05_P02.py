
#nice01 = 'qjhvhtzxzqqjkmpb'
#nice02 = 'xxyxx'
#nice03 = 'uurcxstgmygtbstg'
#nice04 = 'ieodomkazucvgmuy'

nice_str = 0

def check_pairs(input_string):

    #checking if there are repeating pairs
    size = len(input_string)
    for n in range(size-1):
    
        substring = input_string[n:n+2]
        leftover = input_string[n+2:size]
    
        if substring in leftover:
            return True
    return False

def skipping_letter(input_string):

    #checking if a letter repeats with exactly one letter between them
    size = len(input_string)

    for n in range(size-2):
        
        first_letter = input_string[n]
        second_letter = input_string[n+2]
    
        if first_letter == second_letter:
            return True
    return False

with open('Data_d05p01.txt', 'r') as mydata:
    for myline in mydata:
        pairs = check_pairs(myline)
        skip = skipping_letter(myline)

        if pairs == True and skip == True:
            nice_str +=1

print(nice_str)


            