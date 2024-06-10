
def read_input(n):
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    return table

def reconstruct_map(table):
    n = len(table)
    map = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] != 0:
                map[i][j] = table[i][j]
    return map

def find_shortest_path(map, start, end):
    n = len(map)
    visited = [False for _ in range(n)]
    queue = [(start, 0)]
    while queue:
        node, dist = queue.pop(0)
        if node == end:
            return dist
        for i in range(n):
            if map[node][i] != 0 and not visited[i]:
                visited[i] = True
                queue.append((i, dist + map[node][i]))
    return -1

def find_all_paths(map, start, end):
    n = len(map)
    visited = [False for _ in range(n)]
    queue = [(start, 0)]
    paths = []
    while queue:
        node, dist = queue.pop(0)
        if node == end:
            paths.append((start, end))
            return paths
        for i in range(n):
            if map[node][i] != 0 and not visited[i]:
                visited[i] = True
                queue.append((i, dist + map[node][i]))
    return paths

def get_all_roads(map):
    n = len(map)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if map[i][j] != 0:
                roads.append((i+1, j+1))
    return roads

def main():
    n = int(input())
    table = read_input(n)
    map = reconstruct_map(table)
    roads = get_all_roads(map)
    for road in roads:
        print(road[0], road[1])

if __name__ == '__main__':
    main()

