
c = int(input())
edges = [list(map(int, input().split())) for _ in range(c)]
players = [input().split() for _ in range(10)]

# Function to calculate synergy score between two players
def calculate_synergy(player1, player2):
    synergy = 0
    if player1[1] == player2[1]:  # Same country
        synergy += 1
    if player1[2] == player2[2]:  # Same league
        synergy += 1
    if player1[3] == player2[3]:  # Same team
        synergy += 2
    if player1[1] == player2[1] and player1[2] == player2[2]:  # Same country and league
        synergy += 1
    if player1[1] == player2[1] and player1[3] == player2[3]:  # Same country and team
        synergy += 2
    return synergy

# Check if perfect team can be organized
possible = True
for edge in edges:
    player1 = players[edge[0]]
    player2 = players[edge[1]]
    if calculate_synergy(player1, player2) < 2:
        possible = False
        break

if possible:
    print("yes")
else:
    print("no")
