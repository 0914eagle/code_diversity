
c = int(input())
edges = [tuple(map(int, input().split())) for _ in range(c)]
players = [input().split()[1] for _ in range(10)]

def get_synergy_score(player1, player2):
    score = 0
    if player1 == player2:
        score = 3
    elif player1.split()[1] == player2.split()[1]:
        score = 1
    if player1.split()[2] == player2.split()[2]:
        score += 1
    if player1.split()[3] == player2.split()[3]:
        score += 2
    return score

def is_perfect_team_possible():
    for i in range(10):
        degree = sum(1 for edge in edges if i in edge)
        total_synergy = sum(get_synergy_score(players[i], players[j]) for j in range(10) if (i, j) in edges or (j, i) in edges)
        if total_synergy < degree:
            return "no"
    return "yes"

print(is_perfect_team_possible())
