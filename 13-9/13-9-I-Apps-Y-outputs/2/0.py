
def get_next_letter(letter):
    return chr(ord(letter) + 1)

def main():
    letter = input("Enter a lowercase letter: ")
    if letter.isalpha() and letter.islower() and letter != "z":
        next_letter = get_next_letter(letter)
        print(f"{letter} is followed by {next_letter}.")
    else:
        print("Invalid input.")

if __name__ == '__main__':
    main()

