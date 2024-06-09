
import sys

def dijkstra(graph, start, end):
    # Dijkstra's algorithm
    dist = [float('inf') for _ in range(len(graph))]
    dist[start] = 0
    prev = [None for _ in range(len(graph))]
    q = [(0, start)]
    while q:
        cost, u = heapq.heappop(q)
        if dist[u] < cost:
            continue
        for v, c in graph[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                prev[v] = u
                heapq.heappush(q, (dist[v], v))
    return dist, prev

def shortest_paths(graph, start, end):
    dist, prev = dijkstra(graph, start, end)
    paths = []
    u = end
    while u is not None:
        path = []
        while u is not None:
            path.append(u)
            u = prev[u]
        paths.append(path[::-1])
        u = prev[end]
    return paths

def main():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    s, t = map(int, input().split())
    paths = shortest_paths(graph, s, t)
    print(len(paths))

if __name__ == '__main__':
    main()

