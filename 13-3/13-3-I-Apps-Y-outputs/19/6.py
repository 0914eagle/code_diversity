
def is_fair_game(words):
    if len(words) < 2:
        return "Fair Game"
    prev_word = words[0]
    for i in range(1, len(words)):
        if not words[i].startswith(prev_word[-1]):
            return "Player " + str(i % 2 + 1) + " lost"
        prev_word = words[i]
    return "Fair Game"

def main():
    num_words = int(input())
    words = []
    for i in range(num_words):
        words.append(input())
    print(is_fair_game(words))

if __name__ == '__main__':
    main()

