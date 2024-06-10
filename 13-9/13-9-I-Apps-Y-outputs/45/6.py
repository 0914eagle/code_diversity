
def check_for_double_s(word):
    if "ss" in word:
        return "hiss"
    else:
        return "no hiss"

def main():
    word = input("Enter a word: ")
    print(check_for_double_s(word))

if __name__ == '__main__':
    main()

