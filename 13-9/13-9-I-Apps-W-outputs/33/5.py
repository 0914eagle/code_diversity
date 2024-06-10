
def get_input():
    R, C = map(int, input().split())
    assert 1 <= R <= 50 and 1 <= C <= 50
    map = [input() for _ in range(R)]
    assert all(len(row) == C for row in map)
    assert 'D' in map[0] and 'S' in map[0]
    assert all(c in '.X*' for row in map for c in row)
    return R, C, map

def is_safe(R, C, map, r, c):
    if r < 0 or r >= R or c < 0 or c >= C:
        return False
    if map[r][c] == 'X':
        return False
    if map[r][c] == '*' and (r, c) not in safe_places:
        return False
    return True

def bfs(R, C, map, r, c):
    queue = [(r, c)]
    visited = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if map[r][c] == 'D':
            return True
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if is_safe(R, C, map, nr, nc):
                queue.append((nr, nc))
    return False

def solve(R, C, map):
    safe_places = set()
    for r in range(R):
        for c in range(C):
            if map[r][c] == '.':
                safe_places.add((r, c))
    for r in range(R):
        for c in range(C):
            if map[r][c] == '*':
                if bfs(R, C, map, r, c):
                    return 'KAKTUS'
    return -1

def main():
    R, C, map = get_input()
    print(solve(R, C, map))

if __name__ == '__main__':
    main()

