
def input_letter():
    alpha = input()
    return alpha

def check_case(letter):
    if letter.isupper():
        return "A"
    else:
        return "a"

def main():
    letter = input_letter()
    result = check_case(letter)
    print(result)

if __name__ == '__main__':
    main()

