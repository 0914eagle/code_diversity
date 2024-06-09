
# Read input
n, m = map(int, input().split())
dance_grid = [input() for _ in range(n)]

# Count the number of moves
moves = 0
for j in range(m):
    if all(dance_grid[i][j] == '_' for i in range(n)):
        moves += 1

# Output the result
print(moves)
