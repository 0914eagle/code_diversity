
import sys
import math

def is_leaf(node, graph):
    return len(graph[node]) == 1

def is_simple_path(u, v, graph):
    visited = set()
    queue = [u]
    while queue:
        node = queue.pop(0)
        if node == v:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def can_reach_value(graph, value):
    queue = [(1, 0)]
    visited = set()
    while queue:
        node, cost = queue.pop(0)
        if node == len(graph):
            return True
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, cost + weight))
    return False

def solve(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    return "YES" if can_reach_value(graph, 0) else "NO"

if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(solve(n, edges))

