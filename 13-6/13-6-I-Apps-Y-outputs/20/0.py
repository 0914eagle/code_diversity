
def is_vowel(c):
    vowels = ["a", "e", "i", "o", "u"]
    if c in vowels:
        return "vowel"
    else:
        return "consonant"

def main():
    c = input("Enter a lowercase English letter: ")
    print(is_vowel(c))

if __name__ == '__main__':
    main()

