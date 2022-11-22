import string
import caesercipher
import enchant

# key = bcdefghijklmnopqrstuvwxyza
# alp = abcdefghijklmnopqrstuvwxyz

normal_alphabet = string.ascii_lowercase

dictionary = enchant.Dict("en_US")

def encrypt(message, key):
    result = ''

    for char in message:
        capital = char.isupper()
        use_char = char.lower()
        loc = normal_alphabet.find(use_char)
        letter = char in normal_alphabet
        if letter == True:
            if capital == True:
                result += key[loc].upper()
            if capital == False:
                result += key[loc].lower()
        else:
            result += char

    return result

def decrypt(message, key):
    result = ''

    for char in message:
        capital = char.isupper()
        use_char = char.lower()
        loc = key.find(use_char)
        letter = char in normal_alphabet
        if letter == True:
            if capital == True:
                result += normal_alphabet[loc].upper()
            if capital == False:
                result += normal_alphabet[loc].lower()
        else:
            result += char
    
    return result

# TODO make solving function...


print(encrypt("Hello stupid!", "bcdefghijklmnopqrstuvwxyza"))
print(solve_substitution("gsv jfrxp yildm ulc qfnkh levi gsrigvvm ozab wlth"))