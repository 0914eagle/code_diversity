
def get_smallest_missing_letter(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string:
            return char
    return "None"

def main():
    string = input()
    print(get_smallest_missing_letter(string))

if __name__ == '__main__':
    main()

