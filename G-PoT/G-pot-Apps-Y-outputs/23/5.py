
def is_safe(grid, x, y):
    if grid[y][x] == 'T':
        return False
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == 'T':
            return False
    return True

def find_optimal_gold(grid):
    player_pos = None
    gold_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'P':
                player_pos = (x, y)
            elif grid[y][x] == 'G' and is_safe(grid, x, y):
                gold_count += 1
    return gold_count

W, H = map(int, input().split())
grid = [input() for _ in range(H)]

print(find_optimal_gold(grid))
