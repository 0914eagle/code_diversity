
def get_input():
    N = int(input())
    word = input()
    return N, word

def is_possible_to_win(word):
    if len(word) % 2 == 0:
        return "DA"
    else:
        return "NE"

def get_most_beautiful_word(word):
    return "".join(sorted(word))

if __name__ == '__main__':
    N, word = get_input()
    print(is_possible_to_win(word))
    print(get_most_beautiful_word(word))

