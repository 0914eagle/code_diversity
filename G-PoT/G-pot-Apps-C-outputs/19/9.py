
# Read input
R, C = map(int, input().split())
grid = [input() for _ in range(R)]

# Function to check if a building can be disarmed
def can_disarm(row, col):
    for i in range(R):
        if i != row and grid[i][col] == 'x':
            return True
    for j in range(C):
        if j != col and grid[row][j] == 'x':
            return True
    return False

# Count the maximum number of buildings that can be disarmed
count = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'x' and can_disarm(i, j):
            count += 1

# Print the result
print(count)
