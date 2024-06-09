
W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]

def is_safe(x, y):
    if x < 0 or x >= W or y < 0 or y >= H or grid[y][x] == '#':
        return False
    return True

def count_gold(x, y):
    count = 0
    if grid[y][x] == 'G':
        count += 1
    grid[y][x] = '#'  # Mark the current position as visited
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if is_safe(new_x, new_y):
            count += count_gold(new_x, new_y)
    return count

player_x, player_y = 0, 0
for y in range(H):
    for x in range(W):
        if grid[y][x] == 'P':
            player_x, player_y = x, y

print(count_gold(player_x, player_y))
