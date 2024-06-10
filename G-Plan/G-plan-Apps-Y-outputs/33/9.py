
def coconut_splat_winner(s, n):
    players = [i for i in range(1, n + 1)]
    current_player = 0

    while len(players) > 1:
        current_player = (current_player + s - 1) % len(players)
        action = players[current_player]

        if action % 2 == 0:
            players.pop(current_player)
        else:
            players.insert(0, players.pop(current_player))

    return players[0]

if __name__ == '__main__':
    s, n = map(int, input().split())
    print(coconut_splat_winner(s, n))
