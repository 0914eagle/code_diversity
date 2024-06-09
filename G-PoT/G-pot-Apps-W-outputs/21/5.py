
c = int(input())
connections = [list(map(int, input().split())) for _ in range(c)]
players = [input().split() for _ in range(10)]

def get_synergy_score(player1, player2):
    score = 0
    if player1[1] == player2[1]:  # same country
        score += 1
    if player1[2] == player2[2]:  # same league
        score += 1
    if player1[3] == player2[3]:  # same team
        score += 2
    if player1[1] == player2[1] and player1[2] == player2[2]:  # same country and league
        score += 1
    if player1[1] == player2[1] and player1[3] == player2[3]:  # same country and team
        score += 2
    return score

def is_perfect_team(formation, players):
    for i in range(10):
        total_synergy = sum(get_synergy_score(players[i], players[j]) for j in formation[i])
        if total_synergy < len(formation[i]):
            return "no"
    return "yes"

formation = [[] for _ in range(10)]
for a, b in connections:
    formation[a].append(b)
    formation[b].append(a)

print(is_perfect_team(formation, players))
