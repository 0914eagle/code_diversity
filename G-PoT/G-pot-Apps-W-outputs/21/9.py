
# Read input
c = int(input())
edges = [tuple(map(int, input().split())) for _ in range(c)]
players = [input().split() for _ in range(10)]

# Create a dictionary to store player information
player_info = {}
for player in players:
    player_info[player[0]] = player[1:]

# Check if a perfect team can be organized
possible = True
for edge in edges:
    player1, player2 = players[edge[0]], players[edge[1]]
    synergy_score = 0
    
    if player1[1] == player2[1]:  # Same country
        synergy_score += 1
    if player1[2] == player2[2]:  # Same league
        synergy_score += 1
    if player1[3] == player2[3]:  # Same team
        synergy_score += 2
    if player1[1] == player2[1] and player1[2] == player2[2]:  # Same country and league
        synergy_score += 1
    if player1[1] == player2[1] and player1[3] == player2[3]:  # Same country and team
        synergy_score += 2
    
    if synergy_score < 2:
        possible = False
        break

if possible:
    print("yes")
else:
    print("no")
