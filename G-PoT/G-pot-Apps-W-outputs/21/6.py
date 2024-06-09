
c = int(input())
edges = [tuple(map(int, input().split())) for _ in range(c)]
players = [input().split()[1] for _ in range(10)]

def synergy_score(player1, player2):
    if player1 == player2:
        return 3
    else:
        return 1

def is_perfect_team_possible():
    for i in range(10):
        degree = sum(1 for edge in edges if i in edge)
        synergy_sum = sum(synergy_score(players[i], players[j]) for j in range(10) if (i, j) in edges or (j, i) in edges)
        if synergy_sum < degree:
            return "no"
    return "yes"

print(is_perfect_team_possible())
