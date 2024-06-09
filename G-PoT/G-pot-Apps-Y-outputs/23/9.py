
# Read input
W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# Find player's starting position
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'P':
            player_pos = (i, j)
            break

# Define function to check if a position is safe
def is_safe(pos):
    i, j = pos
    if i < 0 or i >= H or j < 0 or j >= W:
        return False
    if grid[i][j] == '#' or grid[i][j] == 'T':
        return False
    return True

# Define function to find adjacent safe positions
def adjacent_safe_positions(pos):
    i, j = pos
    adj_positions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [adj_pos for adj_pos in adj_positions if is_safe(adj_pos)]

# Define function to recursively explore the grid
def explore(pos):
    i, j = pos
    if grid[i][j] == 'G':
        return 1
    grid[i][j] = '#'  # Mark current position as visited
    total_gold = 0
    for adj_pos in adjacent_safe_positions(pos):
        total_gold += explore(adj_pos)
    return total_gold

# Start the exploration from the player's starting position
total_gold = explore(player_pos)

print(total_gold)
