
def check_hiss(word):
    if "ss" in word:
        return "hiss"
    else:
        return "no hiss"

def main():
    word = input("Enter a word: ")
    print(check_hiss(word))

if __name__ == '__main__':
    main()

