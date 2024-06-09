
def get_most_beautiful_word(word):
    return "".join(sorted(word))

def is_winning_move(word, remaining_letters):
    return len(remaining_letters) == 0 or get_most_beautiful_word(word + remaining_letters[-1]) > get_most_beautiful_word(word)

def get_winning_move(word, remaining_letters):
    if len(remaining_letters) == 0:
        return "NE"
    if is_winning_move(word, remaining_letters):
        return "DA", get_most_beautiful_word(word + remaining_letters[-1])
    return "NE", ""

def main():
    n = int(input())
    word = input()
    remaining_letters = list(word)
    result = get_winning_move("", remaining_letters)
    print(result[0])
    print(result[1])

if __name__ == '__main__':
    main()

