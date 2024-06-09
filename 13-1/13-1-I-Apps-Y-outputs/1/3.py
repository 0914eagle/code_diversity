
import heapq

def dijkstra(graph, start, end):
    visited = set()
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while queue:
        (dist, node) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return distances[node]
            for neighbor, weight in graph[node].items():
                distance = dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return float('inf')

def solve(graph, start, end, k):
    distances = []
    for node in graph:
        if node != start:
            distance = dijkstra(graph, start, node)
            distances.append((distance, node))

    distances.sort()
    return distances[k-1][0]

def main():
    n, m, k = map(int, input().split())
    graph = {}
    for _ in range(m):
        x, y, w = map(int, input().split())
        if x not in graph:
            graph[x] = {}
        if y not in graph:
            graph[y] = {}
        graph[x][y] = w
        graph[y][x] = w

    print(solve(graph, 1, n, k))

if __name__ == '__main__':
    main()

