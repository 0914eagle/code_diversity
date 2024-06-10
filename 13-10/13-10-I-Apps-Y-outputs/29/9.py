
def convert_letter(letter):
    if letter.isupper():
        return "A"
    else:
        return "a"

def main():
    letter = input("Enter a letter: ")
    converted_letter = convert_letter(letter)
    print(converted_letter)

if __name__ == '__main__':
    main()

