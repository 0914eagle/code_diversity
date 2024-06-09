
def solve_tournament(n, m):
    teams = [f"{chr(i)}" for i in range(65, 65 + m)]
    players = [f"{team}{i}" for team in teams for i in range(1, n + 1)]
    rounds = []
    for i in range(n * (m - 1) + 1):
        game = []
        for j in range(m):
            if j == 0:
                game.append(f"{players[i]}-{players[i + j * n]}")
            elif j == m - 1:
                game.append(f"{players[i]}-{players[i + j * n]}")
            else:
                game.append(f"{players[i]}-{players[i + j * n]}")
                game.append(f"{players[i + (j - 1) * n]}-{players[i + j * n]}")
        rounds.append(" ".join(game))
    return "\n".join(rounds)

