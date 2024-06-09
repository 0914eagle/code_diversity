
import sys

def shortest_paths(graph, source, destination):
    visited = [False] * len(graph)
    queue = [[source, 0]]
    visited[source] = True
    while queue:
        (vertex, distance) = queue.pop(0)
        if vertex == destination:
            return distance
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append([neighbor, distance + 1])
    return -1

def count_shortest_paths(graph, source, destination):
    visited = [False] * len(graph)
    queue = [[source, 0]]
    visited[source] = True
    count = 0
    while queue:
        (vertex, distance) = queue.pop(0)
        if vertex == destination:
            count += 1
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append([neighbor, distance + 1])
    return count

def main():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    s, t = map(int, input().split())
    print(count_shortest_paths(graph, s, t))

if __name__ == '__main__':
    main()

