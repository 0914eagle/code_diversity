
def convert_to_upper(letter):
    return letter.upper()

def convert_to_lower(letter):
    return letter.lower()

def main():
    letter = input("Enter a letter: ")
    if letter.isupper():
        print(convert_to_upper(letter))
    else:
        print(convert_to_lower(letter))

if __name__ == '__main__':
    main()

