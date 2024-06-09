
c = int(input())
edges = []
for _ in range(c):
    a, b = map(int, input().split())
    edges.append((a, b))

players = []
for _ in range(10):
    player = input().split()
    players.append(player)

def calculate_synergy(player1, player2):
    synergy = 0
    if player1[1] == player2[1]:  # same country
        synergy += 1
    if player1[2] == player2[2]:  # same league
        synergy += 1
    if player1[3] == player2[3]:  # same team
        synergy += 2
    if player1[1] == player2[1] and player1[2] == player2[2]:  # same country and league
        synergy += 1
    if player1[1] == player2[1] and player1[3] == player2[3]:  # same country and team
        synergy += 3
    return synergy

def is_perfect_team_possible():
    for i in range(10):
        degree = 0
        for edge in edges:
            if i in edge:
                degree += 1
        total_synergy = 0
        for j in range(10):
            if (i, j) in edges or (j, i) in edges:
                total_synergy += calculate_synergy(players[i], players[j])
        if total_synergy < degree:
            return "no"
    return "yes"

print(is_perfect_team_possible())