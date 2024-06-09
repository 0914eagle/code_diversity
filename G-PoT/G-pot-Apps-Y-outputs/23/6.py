
def find_optimal_gold(map):
    def is_valid_move(x, y):
        return 0 <= x < width and 0 <= y < height and map[y][x] != '#'

    def can_get_gold(x, y):
        return map[y][x] == 'G'

    def dfs(x, y):
        if not is_valid_move(x, y) or visited[y][x]:
            return 0
        visited[y][x] = True
        if can_get_gold(x, y):
            return 1
        return dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)

    height = len(map)
    width = len(map[0])
    visited = [[False for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            if map[y][x] == 'P':
                return dfs(x, y)

# Read input
W, H = map(int, input().split())
game_map = [input() for _ in range(H)]

# Find optimal gold
optimal_gold = find_optimal_gold(game_map)
print(optimal_gold)
