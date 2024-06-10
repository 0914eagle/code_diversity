
import sys

def is_acyclic(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)

    # Check if the graph is acyclic
    visited = [False] * n
    stack = []
    for vertex in range(n):
        if not visited[vertex]:
            stack.append(vertex)
            while stack:
                vertex = stack.pop()
                if not visited[vertex]:
                    visited[vertex] = True
                    for neighbor in graph[vertex]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
    return not any(visited)

def remove_edge(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)

    # Remove an edge from the graph
    for edge in edges:
        graph[edge[0] - 1].remove(edge[1] - 1)
        graph[edge[1] - 1].remove(edge[0] - 1)

    # Check if the graph is acyclic
    visited = [False] * n
    stack = []
    for vertex in range(n):
        if not visited[vertex]:
            stack.append(vertex)
            while stack:
                vertex = stack.pop()
                if not visited[vertex]:
                    visited[vertex] = True
                    for neighbor in graph[vertex]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
    return not any(visited)

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    if is_acyclic(n, m, edges):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

