
# Read input
N, M = map(int, input().split())
dance_grid = [input() for _ in range(N)]

# Initialize variables
moves = 0
prev_blank = False

# Count the number of moves
for j in range(M):
    blank = True
    for i in range(N):
        if dance_grid[i][j] == '$':
            blank = False
            break
    if blank and not prev_blank:
        moves += 1
    prev_blank = blank

# Output the result
print(moves)
