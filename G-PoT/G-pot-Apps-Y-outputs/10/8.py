
# Read input
n, m = map(int, input().split())
dance_moves = [input() for _ in range(n)]

# Count number of moves
num_moves = 0
for j in range(m):
    if all(dance_moves[i][j] == '_' for i in range(n)):
        num_moves += 1

# Output the result
print(num_moves)
