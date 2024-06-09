
import sys

sys.setrecursionlimit(10000)

def dijkstra(graph, src):
    dist = [float('inf') for _ in range(len(graph))]
    dist[src] = 0
    visited = [False for _ in range(len(graph))]

    pq = [(0, src)]
    while pq:
        dist_u, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in graph[u]:
            if dist[v] > dist_u + w:
                dist[v] = dist_u + w
                heapq.heappush(pq, (dist[v], v))

    return dist

def number_of_shortest_paths(graph, src, dest):
    dist = dijkstra(graph, src)
    return dist[dest]

def count_shortest_paths(graph):
    result = []
    for u in range(len(graph)):
        count = 0
        for v in range(len(graph)):
            if number_of_shortest_paths(graph, u, v) == 1:
                count += 1
        result.append(count)
    return result

def main():
    num_cities, num_roads = map(int, input().split())
    graph = [[] for _ in range(num_cities)]
    for _ in range(num_roads):
        origin, destination, length = map(int, input().split())
        graph[origin].append((destination, length))

    result = count_shortest_paths(graph)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()

