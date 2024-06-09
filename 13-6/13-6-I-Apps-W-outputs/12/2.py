
import sys

def get_input():
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w
    s, t = map(int, input().split())
    return V, E, graph, s, t

def bfs(graph, s, t):
    queue = [s]
    visited = set()
    distance = {}
    while queue:
        u = queue.pop(0)
        if u not in visited:
            visited.add(u)
            if u == t:
                return distance[u]
            for v in graph[u]:
                if v not in visited:
                    queue.append(v)
                    distance[v] = distance[u] + graph[u][v]
    return -1

def shortest_paths(graph, s, t):
    queue = [s]
    visited = set()
    distance = {}
    paths = []
    while queue:
        u = queue.pop(0)
        if u not in visited:
            visited.add(u)
            if u == t:
                paths.append(distance[u])
            for v in graph[u]:
                if v not in visited:
                    queue.append(v)
                    distance[v] = distance[u] + graph[u][v]
    return len(paths)

def main():
    V, E, graph, s, t = get_input()
    print(shortest_paths(graph, s, t))

if __name__ == '__main__':
    main()

