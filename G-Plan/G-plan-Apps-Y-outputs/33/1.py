
def simulate_coconut_splat(s, n):
    players = [True] * n
    current_player = 0

    for _ in range(n - 1):
        steps = s % sum(players)
        while steps > 0:
            if players[current_player]:
                steps -= 1
            current_player = (current_player + 1) % n

        while not players[current_player]:
            current_player = (current_player + 1) % n

        players[current_player] = False

    return players.index(True) + 1

if __name__ == "__main__":
    s, n = map(int, input().split())
    print(simulate_coconut_splat(s, n))
