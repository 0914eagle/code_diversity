
import sys
import queue

def dfs(graph, start, visited, order):
    visited[start] = True
    order.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, order)

def build_graph(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def get_min_time(graph, order):
    min_time = sys.maxsize
    for node in order:
        if graph[node][0] != -1:
            min_time = min(min_time, graph[node][0])
    return min_time

def solve(n, k, a, edges):
    graph = build_graph(n, edges)
    order = []
    visited = [False] * (n + 1)
    dfs(graph, 1, visited, order)
    order = order[:k]
    return get_min_time(graph, order)

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(solve(n, k, a, edges))

if __name__ == '__main__':
    main()

