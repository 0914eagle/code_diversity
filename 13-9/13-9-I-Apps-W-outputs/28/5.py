
import sys

def is_acyclic(graph):
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            visited.add(node)
            stack.append(node)
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
    return len(visited) == len(graph)

def remove_edge(graph):
    for node in graph:
        for neighbor in graph[node]:
            if graph[node].index(neighbor) != len(graph[node]) - 1:
                graph[node].remove(neighbor)
                return graph
    return graph

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    if is_acyclic(graph):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

