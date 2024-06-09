
def is_safe(grid, x, y):
    if grid[y][x] == 'T':
        return False
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if grid[y+dy][x+dx] == 'T':
                return False
    return True

def count_gold(grid):
    gold_count = 0
    for row in grid:
        gold_count += row.count('G')
    return gold_count

W, H = map(int, input().split())
grid = [input() for _ in range(H)]

player_x, player_y = 0, 0
for y in range(H):
    for x in range(W):
        if grid[y][x] == 'P':
            player_x, player_y = x, y

safe_gold = 0
for dy in range(-1, 2):
    for dx in range(-1, 2):
        if grid[player_y+dy][player_x+dx] == 'G' and is_safe(grid, player_x+dx, player_y+dy):
            safe_gold += 1

print(safe_gold)
