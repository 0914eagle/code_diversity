
def schedule_tournament(n, m):
    teams = [f"Team {i+1}" for i in range(m)]
    players = [f"Player {i+1}" for i in range(n)]
    schedule = []
    for i in range(m-1):
        for j in range(i+1, m):
            schedule.append([(teams[i], players[j-i-1]), (teams[j], players[i])])
    return schedule

