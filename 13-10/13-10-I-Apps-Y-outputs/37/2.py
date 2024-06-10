
def find_smallest_missing_letter(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in s:
            return letter
    return "None"

def main():
    s = input()
    print(find_smallest_missing_letter(s))

if __name__ == '__main__':
    main()

