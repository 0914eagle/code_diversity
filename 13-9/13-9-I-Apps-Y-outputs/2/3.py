
def get_next_letter(letter):
    return chr(ord(letter) + 1)

def main():
    letter = input("Enter a lowercase English letter that is not z: ")
    next_letter = get_next_letter(letter)
    print(f"{letter} is followed by {next_letter}.")

if __name__ == '__main__':
    main()

