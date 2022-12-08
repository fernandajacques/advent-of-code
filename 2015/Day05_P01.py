
nice01 = 'ugknbfddgicrmopn'
nice02 = 'aaa'
nice03 = 'jchzalrnumimnmhp'
nice04 = 'haegwjzuvuyypxyu'
nice05 = 'dvszwmarrgswjxmb'

nice_str = 0

def disallowed_check(input_string):

    #check if there are any of the disallowed substrings
    disallowed = ['ab', 'cd', 'pq', 'xy']
    for dis in disallowed:
        if dis in input_string:
            return False
    return True

def vowels_checking(input_string):

    #check if there are at least three vowels
    vowels = set('aeiou')
    vowel_count = 0

    for letter in input_string:
        if letter in vowels:
            vowel_count +=1

    return vowel_count

def double_letters(input_string):    
    
    #check double letters
    for letter in input_string:
        double_letter = letter + letter
        if double_letter in input_string:
            return True
    return False


with open('Data_d05p01.txt', 'r') as mydata:
    for myline in mydata:

        checking = disallowed_check(myline)
        vowels = vowels_checking(myline)
        doubles = double_letters(myline)

        if checking == True and vowels > 2 and doubles == True:

            nice_str +=1

print(nice_str)


            