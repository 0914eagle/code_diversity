
def find_optimal_gold(map):
    def is_safe(x, y):
        if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
            return False
        if map[y][x] == 'T':
            return False
        return True

    def explore(x, y):
        if not is_safe(x, y):
            return 0
        if map[y][x] == 'G':
            return 1
        if map[y][x] == '#':
            return 0

        map[y][x] = '#'  # mark as visited
        total_gold = 0
        total_gold += explore(x + 1, y)
        total_gold += explore(x - 1, y)
        total_gold += explore(x, y + 1)
        total_gold += explore(x, y - 1)

        return total_gold

    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'P':
                return explore(x, y)

# Read input
W, H = map(int, input().split())
game_map = [list(input()) for _ in range(H)]

# Find optimal gold
optimal_gold = find_optimal_gold(game_map)

# Output
print(optimal_gold)
