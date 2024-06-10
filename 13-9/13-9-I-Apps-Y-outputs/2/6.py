
def get_next_letter(letter):
    return chr(ord(letter) + 1)

def main():
    letter = input("Enter a lowercase letter: ")
    if letter.islower() and letter != "z":
        print(get_next_letter(letter))
    else:
        print("Invalid input")

if __name__ == '__main__':
    main()

