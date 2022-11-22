import string
import enchant

dictionary = enchant.Dict("en_US")

normal_alphabet = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


def solve_caeser(text_to_solve):
    for i in range(len(''.join(normal_alphabet))):
        result = caesar(text_to_solve, -i, normal_alphabet)
        words = result.split(" ")
        correct_words = 0
        for word in words:
            correctword = dictionary.check(word)
            if correctword:
                correct_words += 1
        
        if correct_words > 2:
            return result, i


#print(solve_caeser("Nlupbz dpaovba lkbjhapvu pz sprl zpscly pu aol tpul"))