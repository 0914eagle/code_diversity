
def is_possible_to_win(word):
    return "DA" if word[0] == "k" else "NE"

def get_most_beautiful_word(word):
    if word[0] == "k":
        return "ak"
    else:
        return word

if __name__ == '__main__':
    N = int(input())
    word = input()
    print(is_possible_to_win(word))
    print(get_most_beautiful_word(word))

