import enchant

normal_alphabet = 'abcdefghijklmnopqrstuvwxyz'

default_key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def encrypt(message, key):
    result = ''

    res1 = []
    for char in message.lower():
        loc = normal_alphabet.find(char)
        keyInt = key[loc]
        res1.append(keyInt)

    res2 = []
    for val in res1:
        newRes = (val * 5) + 8
        newRes = newRes % 26
        
        res2.append(newRes)
    
    for val in res2:
        newRes = normal_alphabet[val]
        result += newRes

    return result

def decrypt():
    result = ''

result = encrypt("AFFINECIPHER")
print(result)