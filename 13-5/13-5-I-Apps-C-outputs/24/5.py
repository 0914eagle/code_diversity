
def f1(n, word):
    # Your code here
    return "DA" if is_winning_word(word) else "NE"

def f2(n, word):
    # Your code here
    return get_most_beautiful_word(word)

def is_winning_word(word):
    return word[0] == "a"

def get_most_beautiful_word(word):
    return "ak"

if __name__ == '__main__':
    n = int(input())
    word = input()
    print(f1(n, word))
    print(f2(n, word))

