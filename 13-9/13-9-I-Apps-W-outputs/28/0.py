
import sys

def can_make_acyclic(n, edges):
    
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in edges:
        graph[u - 1].append(v - 1)

    # Check if the graph has a cycle
    visited = [False] * n
    rec_stack = [False] * n
    for i in range(n):
        if not visited[i] and not rec_stack[i] and has_cycle(graph, i, visited, rec_stack):
            return False

    return True

def has_cycle(graph, vertex, visited, rec_stack):
    
    if rec_stack[vertex]:
        return True

    if visited[vertex]:
        return False

    visited[vertex] = True
    rec_stack[vertex] = True

    for neighbor in graph[vertex]:
        if has_cycle(graph, neighbor, visited, rec_stack):
            return True

    rec_stack[vertex] = False
    return False

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    print("YES" if can_make_acyclic(n, edges) else "NO")

if __name__ == '__main__':
    main()

