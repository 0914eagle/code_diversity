
def play_coconut_splat(syllables, players):
    hands = [True] * players  # True represents folded hands
    current_player = 0

    while sum(hands) > 1:
        for _ in range(syllables):
            current_player = (current_player + 1) % players
            while not hands[current_player]:
                current_player = (current_player + 1) % players

        if hands[current_player]:
            hands[current_player] = False
        else:
            next_player = (current_player + 1) % players
            while not hands[next_player]:
                next_player = (next_player + 1) % players
            hands[next_player] = False

    return hands.index(True) + 1

if __name__ == '__main__':
    syllables, players = map(int, input().split())
    winner = play_coconut_splat(syllables, players)
    print(winner)
