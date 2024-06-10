
def coconut_splat_winner(s, n):
    players = list(range(1, n + 1))
    hands = [True] * n

    current_player = 0
    while len(players) > 1:
        current_player = (current_player + s - 1) % len(players)
        touched_player = players[current_player]

        if hands[current_player]:
            hands[current_player] = False
        elif not hands[current_player]:
            players.pop(current_player)
            hands.pop(current_player)
            current_player -= 1

    return players[0]

if __name__ == '__main__':
    s, n = map(int, input().split())
    print(coconut_splat_winner(s, n))
