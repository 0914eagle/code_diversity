
def get_most_beautiful_word(sequence):
    return "".join(sorted(sequence))

def is_winning_move(sequence, word):
    return len(sequence) == 0 or get_most_beautiful_word(sequence) > word

def get_winning_move(sequence):
    if len(sequence) == 0:
        return "NE"
    word = ""
    while len(sequence) > 0:
        word += sequence.pop()
        if is_winning_move(sequence, word):
            return "DA", word
    return "NE", word

if __name__ == '__main__':
    n = int(input())
    sequence = input()
    print(*get_winning_move(sequence))

