
def get_next_letter(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = alphabet.index(letter)
    return alphabet[index + 1]

def main():
    letter = input("Enter a lowercase English letter: ")
    print(get_next_letter(letter))

if __name__ == '__main__':
    main()

