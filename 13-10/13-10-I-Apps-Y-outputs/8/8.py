
import math
import sys

def find_roads(table):
    n = len(table)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if table[i][j] != 0:
                roads.append([i+1, j+1])
    return roads

def construct_map(roads):
    n = len(roads)
    map = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        u, v = roads[i]
        map[u][v] = 1
        map[v][u] = 1
    return map

def find_shortest_path(map, start, end):
    n = len(map)
    queue = [(0, start)]
    visited = [False] * (n+1)
    while queue:
        dist, curr = queue.pop(0)
        if curr == end:
            return dist
        for i in range(1, n+1):
            if map[curr][i] == 1 and not visited[i]:
                queue.append((dist+1, i))
                visited[i] = True
    return -1

def reconstruct_map(table):
    n = len(table)
    roads = find_roads(table)
    map = construct_map(roads)
    for i in range(n):
        for j in range(i+1, n):
            if table[i][j] != 0 and map[i+1][j+1] == 0:
                dist = find_shortest_path(map, i+1, j+1)
                if dist != -1:
                    map[i+1][j+1] = 1
                    map[j+1][i+1] = 1
    return map

def main():
    n = int(input())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    map = reconstruct_map(table)
    roads = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if map[i][j] == 1:
                roads.append([i, j])
    for road in roads:
        print(" ".join(map(str, road)))

if __name__ == '__main__':
    main()

