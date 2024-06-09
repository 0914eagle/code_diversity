
c = int(input())
edges = []
for _ in range(c):
    a, b = map(int, input().split())
    edges.append((a, b))

players = []
for _ in range(10):
    player_info = input().split()
    players.append(player_info)

def calculate_synergy(player1, player2):
    synergy = 0
    if player1[1] == player2[1]:
        synergy += 1
    if player1[2] == player2[2]:
        synergy += 1
    if player1[3] == player2[3]:
        synergy += 2
    if player1[1] == player2[1] and player1[2] == player2[2]:
        synergy += 1
    if player1[1] == player2[1] and player1[3] == player2[3]:
        synergy += 3
    return synergy

def is_perfect_team_possible(players, edges):
    for edge in edges:
        player1 = players[edge[0]]
        player2 = players[edge[1]]
        if calculate_synergy(player1, player2) < 2:
            return "no"
    return "yes"

print(is_perfect_team_possible(players, edges))
