
# Read input
R, C = map(int, input().split())
grid = [input() for _ in range(R)]

# Initialize variables
row_counts = [0] * R
col_counts = [0] * C

# Count the number of armed buildings in each row and column
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'x':
            row_counts[i] += 1
            col_counts[j] += 1

# Calculate the maximum number of buildings that can be disarmed
max_disarmed = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'x' and (row_counts[i] > 1 or col_counts[j] > 1):
            max_disarmed += 1

print(max_disarmed)
