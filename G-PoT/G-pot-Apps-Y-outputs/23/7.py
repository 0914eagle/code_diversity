
W, H = map(int, input().split())
game_map = [input() for _ in range(H)]

def is_valid_move(x, y):
    return 0 <= x < W and 0 <= y < H

def can_get_gold(x, y):
    if not is_valid_move(x, y) or game_map[y][x] == '#' or game_map[y][x] == 'T':
        return False
    return game_map[y][x] == 'G'

def explore(x, y):
    visited = set()
    stack = [(x, y)]
    gold_count = 0

    while stack:
        curr_x, curr_y = stack.pop()
        if (curr_x, curr_y) in visited:
            continue

        visited.add((curr_x, curr_y))

        if can_get_gold(curr_x, curr_y):
            gold_count += 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = curr_x + dx, curr_y + dy
            if is_valid_move(next_x, next_y) and game_map[next_y][next_x] != '#':
                stack.append((next_x, next_y))

    return gold_count

player_x, player_y = 0, 0
for y in range(H):
    for x in range(W):
        if game_map[y][x] == 'P':
            player_x, player_y = x, y

print(explore(player_x, player_y))
