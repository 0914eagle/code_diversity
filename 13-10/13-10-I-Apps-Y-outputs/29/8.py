
def convert_letter(letter):
    if letter.isupper():
        return "A"
    else:
        return "a"

def main():
    letter = input("Enter a letter: ")
    print(convert_letter(letter))

if __name__ == '__main__':
    main()

