
def schedule_tournament(n, m):
    teams = [f"A{i+1}" for i in range(n)]
    schedule = []
    for i in range(n):
        for j in range(i+1, n):
            schedule.append(f"{teams[i]}-{teams[j]}")
    for k in range(m-1):
        schedule.append("BYE")
    return schedule

