
import sys
sys.setrecursionlimit(10000)

def dijkstra(graph, start):
    visited = [False] * len(graph)
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    path = [None] * len(graph)

    while True:
        u = -1
        for i in range(len(graph)):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        if u == -1:
            break

        visited[u] = True
        for v in range(len(graph[u])):
            if not visited[v] and graph[u][v] != 0 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                path[v] = u

    return dist, path

def find_path(graph, start, end):
    dist, path = dijkstra(graph, start)
    if dist[end] == float('inf'):
        return None

    node = end
    path_list = []
    while node != start:
        path_list.append(node)
        node = path[node]
    path_list.append(start)
    path_list.reverse()
    return path_list

def find_min_time(graph, start, end, people):
    path = find_path(graph, start, end)
    if path is None:
        return -1

    time = 0
    for i in range(len(path) - 1):
        time += graph[path[i]][path[i+1]]

    if time > people:
        return -1

    return time

def get_min_time(graph, start, end, people):
    min_time = float('inf')
    for i in range(len(graph)):
        t = find_min_time(graph, start, i, people - 1)
        if t != -1:
            min_time = min(min_time, t + find_min_time(graph, i, end, people - 1))

    return min_time

def main():
    people, boulders, logs = map(int, input().split())
    graph = [[0] * (boulders + 2) for _ in range(boulders + 2)]

    for _ in range(logs):
        start, end = map(int, input().split())
        graph[start][end] = 1
        graph[end][start] = 1

    graph[-2][0] = 1
    graph[0][-1] = 1

    min_time = get_min_time(graph, -2, -1, people)
    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time)

if __name__ == '__main__':
    main()

