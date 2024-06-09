
W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]

def is_valid(x, y):
    return 0 <= x < W and 0 <= y < H

def can_get_gold(x, y):
    if not is_valid(x, y) or grid[y][x] == '#' or grid[y][x] == 'T':
        return False
    if grid[y][x] == 'G':
        return True
    grid[y][x] = '#'  # Mark as visited
    if can_get_gold(x+1, y) or can_get_gold(x-1, y) or can_get_gold(x, y+1) or can_get_gold(x, y-1):
        return True
    return False

for y in range(H):
    for x in range(W):
        if grid[y][x] == 'P':
            start_x, start_y = x, y

gold_count = 0
if can_get_gold(start_x, start_y):
    gold_count += 1

print(gold_count)
