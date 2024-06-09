
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
    visited = [False] * len(map)
    queue = [(start, 0)]
    while queue:
        node, distance = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        if node == end:
            return distance
        for neighbor in range(len(map)):
            if map[node][neighbor] != 0 and not visited[neighbor]:
                queue.append((neighbor, distance + map[node][neighbor]))
    return -1

def find_roads(map):
    n = len(map)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if map[i][j] != 0:
                roads.append((i+1, j+1))
    return roads

def main():
    n = int(input())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    map = reconstruct_map(table)
    roads = find_roads(map)
    for road in roads:
        print(*road)

if __name__ == "__main__":
    main()

