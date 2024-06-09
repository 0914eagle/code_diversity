
# Read input
R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

# Function to check if a building can be disarmed
def can_disarm(row, col):
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "x" and (r == row or c == col):
                return True
    return False

# Initialize count of disarmed buildings
count = 0

# Iterate through each building in the grid
for r in range(R):
    for c in range(C):
        if grid[r][c] == "x" and can_disarm(r, c):
            count += 1

# Print the maximum number of buildings that can be disarmed
print(count)
