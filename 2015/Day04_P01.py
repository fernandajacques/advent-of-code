
key01 = 'abcdef609043'
key02 = 'pqrstuv1048970'
key03 = 'iwrupvqb'

count = 0
hexadec = True

import hashlib 

while hexadec:

    key = key03 + str(count)
    #print(key)
    result = hashlib.md5(key.encode())
    res_hex = result.hexdigest()
    
    if res_hex[0:5] == '00000':
        print(res_hex)
        print(count)
        hexadec = False

    count +=1

