
def get_letter():
    return input()

def is_uppercase(letter):
    return letter.isupper()

def convert_letter(letter):
    if is_uppercase(letter):
        return "A"
    else:
        return "a"

def main():
    letter = get_letter()
    print(convert_letter(letter))

if __name__ == '__main__':
    main()

