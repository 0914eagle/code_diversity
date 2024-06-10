
def read_map(R, C):
    map = []
    for i in range(R):
        map.append(input().strip())
    return map

def get_neighbors(row, col, map):
    neighbors = []
    if row > 0 and map[row-1][col] != '*':
        neighbors.append((row-1, col))
    if row < len(map)-1 and map[row+1][col] != '*':
        neighbors.append((row+1, col))
    if col > 0 and map[row][col-1] != '*':
        neighbors.append((row, col-1))
    if col < len(map[0])-1 and map[row][col+1] != '*':
        neighbors.append((row, col+1))
    return neighbors

def bfs(map, start, goal):
    queue = [(start, 0)]
    visited = set([start])
    while queue:
        (row, col), time = queue.pop(0)
        if (row, col) == goal:
            return time
        for (new_row, new_col) in get_neighbors(row, col, map):
            if (new_row, new_col) not in visited and map[new_row][new_col] != '*':
                queue.append(((new_row, new_col), time+1))
                visited.add((new_row, new_col))
    return -1

def solve(map):
    R, C = len(map), len(map[0])
    start, goal = None, None
    for i in range(R):
        for j in range(C):
            if map[i][j] == 'S':
                start = (i, j)
            elif map[i][j] == 'D':
                goal = (i, j)
    if not start or not goal:
        return "KAKTUS"
    return bfs(map, start, goal)

def main():
    R, C = map(int, input().split())
    map = read_map(R, C)
    print(solve(map))

if __name__ == '__main__':
    main()

