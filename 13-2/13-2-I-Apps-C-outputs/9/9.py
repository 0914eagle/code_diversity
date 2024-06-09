
def is_winning_word(word):
    return word in ["ak", "ka", "av", "va"]

def get_most_beautiful_word(word):
    return "ak"

def main():
    n = int(input())
    word = input()
    if n % 2 == 0:
        print("NE")
        print(get_most_beautiful_word(word))
    else:
        print("DA")
        print(get_most_beautiful_word(word))

if __name__ == "__main__":
    main()

