
# Read input
r, c = map(int, input().split())
start_bed, fridge = eval(input()), eval(input())
school_map = [input() for _ in range(r)]
p = int(input())
patrol_paths = [list(map(eval, input().split())) for _ in range(p)]

# Function to check if a cell is walkable
def is_walkable(row, col):
    if 0 <= row < r and 0 <= col < c:
        return school_map[row][col] == '.'

# Function to check if the child can reach the fridge without being seen
def can_reach_fridge(row, col, steps):
    if (row, col) == fridge:
        return steps
    if not is_walkable(row, col):
        return float('inf')
    
    min_steps = float('inf')
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if is_walkable(new_row, new_col):
            min_steps = min(min_steps, can_reach_fridge(new_row, new_col, steps + 1))
    
    return min_steps

# Initialize minimum steps to infinity
min_steps = float('inf')

# Iterate through all possible starting positions and calculate minimum steps
for i in range(r):
    for j in range(c):
        if is_walkable(i, j):
            steps = can_reach_fridge(i, j, 0)
            min_steps = min(min_steps, steps)

# Output the result
if min_steps == float('inf'):
    print("IMPOSSIBLE")
else:
    print(min_steps)

