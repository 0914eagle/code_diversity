
# Read input values
N, M = map(int, input().split())
dance_grid = [input() for _ in range(N)]

# Count the number of moves in the dance
moves = 0
for j in range(M):
    if all(dance_grid[i][j] == '_' for i in range(N)):
        moves += 1

# Output the number of moves
print(moves)
