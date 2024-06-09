
def is_winning_word(word):
    return word in ["ak", "ka"]

def get_most_beautiful_word(word):
    return "ak" if word in ["ak", "ka"] else "ka"

def main():
    n = int(input())
    word = input()
    if n % 2 == 0:
        print("NE")
        print(get_most_beautiful_word(word[-1]))
    else:
        print("DA")
        print(get_most_beautiful_word(word[-1]))

if __name__ == '__main__':
    main()

