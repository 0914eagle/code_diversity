
def contains_hiss(word):
    return "hiss" if "ss" in word else "no hiss"

def main():
    word = input("Enter a word: ")
    print(contains_hiss(word))

if __name__ == '__main__':
    main()

