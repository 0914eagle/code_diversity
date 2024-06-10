
import sys

def get_input():
    N = int(input())
    edges = []
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def get_shortest_path(edges, N):
    graph = {i: set() for i in range(1, N + 1)}
    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)
    visited = set()
    queue = [(1, [])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return path

def count_ways(N, edges):
    graph = {i: set() for i in range(1, N + 1)}
    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)
    visited = set()
    count = 0
    for vertex in range(1, N + 1):
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    count += 1
    return count

def solve(N, edges):
    path = get_shortest_path(edges, N)
    return count_ways(N, edges) - count_ways(N, [(x, y) for x, y in edges if x not in path and y not in path])

if __name__ == '__main__':
    N, edges = get_input()
    print(solve(N, edges) % (10**9 + 7))

