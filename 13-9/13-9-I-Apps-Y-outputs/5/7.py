
import sys

def get_input():
    W, H = map(int, input().split())
    assert 3 <= W <= 50 and 3 <= H <= 50
    map = [input() for _ in range(H)]
    assert all(len(line) == W for line in map)
    assert all(line[0] == '#' and line[-1] == '#' for line in map)
    assert 'P' in map[0] and all(line.count('P') == 1 for line in map)
    assert all(c in 'G#.' for line in map for c in line)
    return W, H, map

def find_gold(W, H, map):
    gold = 0
    for y in range(H):
        for x in range(W):
            if map[y][x] == 'G':
                gold += 1
    return gold

def find_traps(W, H, map):
    traps = 0
    for y in range(H):
        for x in range(W):
            if map[y][x] == 'T':
                traps += 1
    return traps

def find_safe_moves(W, H, map, x, y):
    safe_moves = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and map[ny][nx] != '#':
            safe_moves.append((nx, ny))
    return safe_moves

def simulate_game(W, H, map):
    x, y = 0, 0
    while x != W - 1 or y != H - 1:
        safe_moves = find_safe_moves(W, H, map, x, y)
        if not safe_moves:
            return 0
        x, y = safe_moves[0]
        if map[y][x] == 'G':
            map[y][x] = '.'
    return find_gold(W, H, map)

def main():
    W, H, map = get_input()
    print(simulate_game(W, H, map))

if __name__ == '__main__':
    main()

