
def hissing_s(word):
    if "ss" in word:
        return "hiss"
    else:
        return "no hiss"

def main():
    word = input("Enter a word: ")
    print(hissing_s(word))

if __name__ == '__main__':
    main()

