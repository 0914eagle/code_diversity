
import sys
input = sys.stdin.read()

def dijkstra(graph, start, end):
    visited = [False] * len(graph)
    distance = [float('inf')] * len(graph)
    previous = [None] * len(graph)
    queue = [(0, start)]
    visited[start] = True
    distance[start] = 0

    while queue:
        (cost, current) = heapq.heappop(queue)
        if current == end:
            break
        for neighbor, weight in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = cost + weight
                previous[neighbor] = current
                heapq.heappush(queue, (distance[neighbor], neighbor))

    return previous, distance

def shortest_paths(graph, start, end):
    previous, distance = dijkstra(graph, start, end)
    paths = []
    current = end
    while current != start:
        path = []
        while current is not None:
            path.append(current)
            current = previous[current]
        paths.append(path[::-1])
        current = previous[end]
    return paths

def count_shortest_paths(graph, start, end):
    paths = shortest_paths(graph, start, end)
    return len(set(paths)) % 1000000007

def main():
    nodes, roads = map(int, input().split())
    graph = [[] for _ in range(nodes + 1)]
    for _ in range(roads):
        origin, destination, length = map(int, input().split())
        graph[origin].append((destination, length))

    for i in range(1, nodes + 1):
        for j in range(i + 1, nodes + 1):
            count = count_shortest_paths(graph, i, j)
            print(count)

if __name__ == '__main__':
    main()

