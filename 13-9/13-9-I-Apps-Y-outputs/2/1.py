
def get_following_letter(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = alphabet.index(letter)
    following_index = (index + 1) % 26
    following_letter = alphabet[following_index]
    return following_letter

def main():
    letter = input("Enter a lowercase English letter that is not z: ")
    following_letter = get_following_letter(letter)
    print(f"{letter} is followed by {following_letter}.")

if __name__ == '__main__':
    main()

