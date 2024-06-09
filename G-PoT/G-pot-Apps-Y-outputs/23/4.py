
def is_safe(grid, x, y):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False
    return grid[y][x] != 'T'

def get_gold(grid, x, y):
    if not is_safe(grid, x, y):
        return 0
    gold = 0
    if grid[y][x] == 'G':
        gold += 1
    grid[y] = grid[y][:x] + '#' + grid[y][x+1:]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_safe(grid, new_x, new_y):
            gold += get_gold(grid, new_x, new_y)
    return gold

def main():
    w, h = map(int, input().split())
    grid = [input() for _ in range(h)]
    start_x, start_y = next((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'P')
    print(get_gold(grid, start_x, start_y))

if __name__ == "__main__":
    main()
