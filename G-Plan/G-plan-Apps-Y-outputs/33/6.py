
def play_coconut_splat(s, n):
    players = [True] * n
    current_player = 0

    while sum(players) > 1:
        for _ in range(s):
            while not players[current_player]:
                current_player = (current_player + 1) % n
            current_player = (current_player + 1) % n

        while not players[current_player]:
            current_player = (current_player + 1) % n
        players[current_player] = False

    return players.index(True) + 1

if __name__ == '__main__':
    s, n = map(int, input().split())
    print(play_coconut_splat(s, n))
