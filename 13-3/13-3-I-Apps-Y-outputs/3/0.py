
import sys

def reconstruct_map(table):
    n = len(table)
    map = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            map[i][j] = table[i][j]
            map[j][i] = table[i][j]
    return map

def find_shortest_path(map, start, end):
    n = len(map)
    visited = [False] * n
    queue = [(start, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == end:
            return distance
        for i in range(n):
            if map[node][i] != 0 and not visited[i]:
                visited[i] = True
                queue.append((i, distance + map[node][i]))
    return -1

def solve(table):
    map = reconstruct_map(table)
    n = len(map)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if map[i][j] != 0:
                roads.append((i+1, j+1))
    return roads

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    table = []
    for i in range(1, n*n+1, n):
        table.append(data[i:i+n])
    roads = solve(table)
    for road in roads:
        print(*road)

