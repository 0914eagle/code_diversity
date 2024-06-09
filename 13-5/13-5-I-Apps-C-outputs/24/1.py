
def get_most_beautiful_word(word):
    return "".join(sorted(word))

def is_winning_move(word, letter):
    return letter in word

def get_next_word(word, letter):
    return word + letter

def get_beautiful_word(word):
    return get_most_beautiful_word(word)

def solve(word):
    if len(word) == 0:
        return "NE", ""
    letter = word[-1]
    if is_winning_move(word, letter):
        return "DA", get_beautiful_word(get_next_word(word, letter))
    else:
        return "NE", ""

if __name__ == '__main__':
    word = input()
    print(solve(word))

