
def calculate_synergy_score(player1, player2):
    synergy_score = 0
    if player1['nation'] == player2['nation']:
        synergy_score += 1
    if player1['league'] == player2['league']:
        synergy_score += 1
    if player1['team'] == player2['team']:
        synergy_score += 2
    if player1['nation'] == player2['nation'] and player1['league'] == player2['league']:
        synergy_score += 1
    if player1['nation'] == player2['nation'] and player1['team'] == player2['team']:
        synergy_score += 3
    return synergy_score

def is_perfect_team(players, connections):
    for i in range(10):
        player = players[i]
        total_synergy = 0
        for j in range(10):
            if i != j and (i, j) in connections:
                total_synergy += calculate_synergy_score(player, players[j])
        if total_synergy < len(connections):
            return "no"
    return "yes"

c = int(input())
connections = set()
for _ in range(c):
    a, b = map(int, input().split())
    connections.add((a, b))

players = []
for _ in range(10):
    player_info = input().split()
    player = {'name': player_info[0], 'nation': player_info[1], 'league': player_info[2], 'team': player_info[3]}
    players.append(player)

print(is_perfect_team(players, connections))
