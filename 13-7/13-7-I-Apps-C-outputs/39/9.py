
def read_map(N, M):
    map = []
    for i in range(N):
        map.append(list(input()))
    return map

def find_start_and_goal(map):
    start, goal = None, None
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                start = (i, j)
            elif map[i][j] == 'G':
                goal = (i, j)
    return start, goal

def find_shortest_path(map, start, goal):
    visited = set()
    queue = [(start, 0)]
    while queue:
        (i, j), dist = queue.pop(0)
        if (i, j) == goal:
            return dist
        for (ii, jj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < len(map) and 0 <= jj < len(map[0]) and (ii, jj) not in visited and map[ii][jj] != '#':
                visited.add((ii, jj))
                queue.append(((ii, jj), dist+1))
    return -1

def solve(map, start, goal, stamina):
    days = 0
    while start != goal:
        days += 1
        if days % 2 == 0:
            stamina = K
        shortest_path = find_shortest_path(map, start, goal)
        if shortest_path == -1:
            return -1
        start = (start[0] + shortest_path[0], start[1] + shortest_path[1])
        stamina -= shortest_path[2]
        if stamina <= 0:
            return -1
    return days

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    map = read_map(N, M)
    start, goal = find_start_and_goal(map)
    print(solve(map, start, goal, K))

