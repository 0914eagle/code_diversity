
import sys

def get_graph(L):
    graph = {}
    for i in range(L):
        E1, E2 = map(int, input().split())
        if E1 not in graph:
            graph[E1] = []
        if E2 not in graph:
            graph[E2] = []
        graph[E1].append(E2)
        graph[E2].append(E1)
    return graph

def bfs(graph, start, end, visited):
    queue = [[start]]
    visited[start] = True
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(path + [neighbor])
    return []

def get_min_time(graph, start, end, people):
    visited = [False] * (len(graph) + 1)
    time = 0
    while people:
        path = bfs(graph, start, end, visited)
        if not path:
            return -1
        for i in range(len(path) - 1):
            if path[i] != -1 and path[i + 1] != -2:
                time += 1
        people -= 1
        start = path[-1]
    return time

def main():
    P, R, L = map(int, input().split())
    graph = get_graph(L)
    print(get_min_time(graph, -2, -1, P))

if __name__ == '__main__':
    main()

