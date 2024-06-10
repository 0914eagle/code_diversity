
def is_uppercase(letter):
    return letter.isupper()

def convert_letter(letter):
    if is_uppercase(letter):
        return "A"
    else:
        return "a"

if __name__ == '__main__':
    letter = input("Enter a letter: ")
    print(convert_letter(letter))

