import caesercipher

def solve_all(text):
    return caesercipher.solve_caeser(text)

cipher_to_crack = input("Enter cipher you want broken: ")

result = solve_all(cipher_to_crack)

print(f"Result: \'{result[0]}\' Key used: {result[1]}")