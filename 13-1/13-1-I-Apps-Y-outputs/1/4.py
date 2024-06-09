
import heapq

def dijkstra(graph, source, destination):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    visited = set()
    priority_queue = [(0, source)]

    while priority_queue:
        distance, vertex = heapq.heappop(priority_queue)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == destination:
                return distances[destination]
            for neighbor, weight in graph[vertex].items():
                distance_to_neighbor = distance + weight
                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor
                    heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

    return float('inf')

def solve(graph, k):
    distances = []
    for i in range(1, len(graph)):
        for j in range(i+1, len(graph)):
            distance = dijkstra(graph, i, j)
            distances.append(distance)

    distances.sort()
    return distances[k-1]

def main():
    n, m, k = map(int, input().split())
    graph = [{} for _ in range(n+1)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        graph[x][y] = w
        graph[y][x] = w
    print(solve(graph, k))

if __name__ == '__main__':
    main()

