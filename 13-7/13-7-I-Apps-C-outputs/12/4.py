
def schedule_tournament(n, m):
    teams = [f"T{i+1}" for i in range(m)]
    players = [f"P{i+1}" for i in range(n)]
    rounds = []
    for i in range(m-1):
        round_games = []
        for j in range(n):
            home_player = players[j]
            away_player = players[(j+1)%n]
            round_games.append(f"{home_player}-{away_player}")
        rounds.append(" ".join(round_games))
    return "\n".join(rounds)

