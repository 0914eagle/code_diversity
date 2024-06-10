
def read_map(file_name):
    with open(file_name, 'r') as f:
        N, M, K = map(int, f.readline().split())
        map = []
        for _ in range(N):
            map.append(list(f.readline().strip()))
    return N, M, K, map

def find_starting_point(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                return i, j

def find_treasure(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'G':
                return i, j

def is_valid_move(map, i, j, di, dj):
    if i + di < 0 or i + di >= len(map) or j + dj < 0 or j + dj >= len(map[0]):
        return False
    if map[i + di][j + dj] == '#':
        return False
    return True

def bfs(map, starting_point, treasure):
    queue = [(starting_point, 0)]
    visited = set()
    while queue:
        current_point, days = queue.pop(0)
        if current_point == treasure:
            return days
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if is_valid_move(map, current_point[0], current_point[1], di, dj):
                new_point = (current_point[0] + di, current_point[1] + dj)
                if new_point not in visited:
                    visited.add(new_point)
                    queue.append((new_point, days + 1))
    return -1

def solve(map):
    starting_point = find_starting_point(map)
    treasure = find_treasure(map)
    return bfs(map, starting_point, treasure)

if __name__ == '__main__':
    map = read_map('treasure_map.txt')
    print(solve(map))

