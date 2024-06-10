
import sys
sys.setrecursionlimit(10000)

def get_neighbors(graph, vertex):
    neighbors = []
    for v in range(len(graph)):
        if graph[vertex][v] == 1:
            neighbors.append(v)
    return neighbors

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in get_neighbors(graph, vertex):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return visited

def can_escape(graph, pigs, visited):
    for pig in pigs:
        if not visited[pig]:
            return False
    return True

def remove_wolves(graph, pigs, visited, num_wolves):
    if can_escape(graph, pigs, visited):
        return num_wolves
    for i in range(len(pigs)):
        for j in range(i+1, len(pigs)):
            if pigs[i] == pigs[j]:
                continue
            if graph[pigs[i]][pigs[j]] == 1:
                graph[pigs[i]][pigs[j]] = 0
                graph[pigs[j]][pigs[i]] = 0
                visited = bfs(graph, pigs[i], visited)
                num_wolves = remove_wolves(graph, pigs, visited, num_wolves+1)
                graph[pigs[i]][pigs[j]] = 1
                graph[pigs[j]][pigs[i]] = 1
                visited = bfs(graph, pigs[i], visited)
    return num_wolves

def main():
    V, P = map(int, input().split())
    graph = [[0 for _ in range(V)] for _ in range(V)]
    for _ in range(V-1):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    pigs = list(map(int, input().split()))
    visited = [False for _ in range(V)]
    num_wolves = remove_wolves(graph, pigs, visited, 0)
    print(num_wolves)

if __name__ == '__main__':
    main()

