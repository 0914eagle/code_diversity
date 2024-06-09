
# Read input
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

# Function to check if a building can be disarmed
def can_disarm(row, col):
    for i in range(R):
        if grid[i][col] == 'x' and i != row:
            return True
    for j in range(C):
        if grid[row][j] == 'x' and j != col:
            return True
    return False

# Disarm buildings
disarmed_count = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'x' and can_disarm(i, j):
            disarmed_count += 1

print(disarmed_count)
