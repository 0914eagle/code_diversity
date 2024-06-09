
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
        node, dist = queue.pop(0)
        if node == end:
            return dist
        for i in range(n):
            if map[node][i] != 0 and not visited[i]:
                visited[i] = True
                queue.append((i, dist + map[node][i]))
    return -1

def find_all_pairs_shortest_path(map):
    n = len(map)
    all_pairs_shortest_path = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            all_pairs_shortest_path[i][j] = find_shortest_path(map, i, j)
    return all_pairs_shortest_path

def find_roads(all_pairs_shortest_path):
    n = len(all_pairs_shortest_path)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if all_pairs_shortest_path[i][j] != 0:
                roads.append((i+1, j+1))
    return roads

def main():
    n = int(input())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    map = reconstruct_map(table)
    all_pairs_shortest_path = find_all_pairs_shortest_path(map)
    roads = find_roads(all_pairs_shortest_path)
    for road in roads:
        print(road[0], road[1])

if __name__ == "__main__":
    main()

