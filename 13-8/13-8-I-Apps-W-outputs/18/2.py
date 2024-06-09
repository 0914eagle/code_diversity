
def solve(strengths):
    n = len(strengths) // 2
    teams = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            teams[i].append(j)
            teams[j].append(i)
    teammates = [0] * n
    for i in range(n):
        max_strength = 0
        for j in teams[i]:
            if strengths[i][j] > max_strength:
                max_strength = strengths[i][j]
                teammates[i] = j
        teams[teammates[i]].remove(i)
    return teammates

