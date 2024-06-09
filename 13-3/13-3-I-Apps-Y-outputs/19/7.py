
def is_fair_game(words):
    if len(words) < 2:
        return "Fair Game"
    previous_word = words[0]
    for word in words[1:]:
        if word[0] != previous_word[-1]:
            return "Player 1 lost" if word[0] == words[0][-1] else "Player 2 lost"
        previous_word = word
    return "Fair Game"

def main():
    num_words = int(input())
    words = []
    for _ in range(num_words):
        words.append(input())
    print(is_fair_game(words))

if __name__ == '__main__':
    main()

