
import sys

def can_make_acyclic(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)

    # Check if the graph contains a cycle
    visited = [False] * n
    def dfs(node, parent):
        if visited[node]:
            return False
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if dfs(neighbor, node):
                return True
        return False
    for node in range(n):
        if dfs(node, -1):
            return False
    return True

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES") if can_make_acyclic(n, m, edges) else print("NO")

if __name__ == '__main__':
    main()

