
# Read input
N, M = map(int, input().split())
dance_moves = [input() for _ in range(N)]

# Count the number of dance moves
num_moves = 0
for j in range(M):
    if all(dance_moves[i][j] == '_' for i in range(N)):
        num_moves += 1

# Output the result
print(num_moves)
