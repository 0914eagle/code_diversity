
def get_playing_schedule(n, m):
    teams = [f"A{i+1}" for i in range(n)]
    games = []
    for i in range(m-1):
        for j in range(n):
            games.append(f"{teams[j]}-{teams[j+1]}")
        games.append(f"{teams[0]}-{teams[-1]}")
        teams = teams[1:] + teams[:1]
    return "\n".join(games)

