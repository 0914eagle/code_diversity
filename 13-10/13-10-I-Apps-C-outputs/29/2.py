
import math

def find_shortest_path(graph, town):
    visited = set()
    queue = [(0, town)]
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (dist + weight, neighbor))
    return dist

def dijkstra(graph, start):
    dist = {node: math.inf for node in graph}
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if dist < dist[node]:
            continue
        for neighbor, weight in graph[node].items():
            v = dist + weight
            if v < dist[neighbor]:
                dist[neighbor] = v
                heapq.heappush(queue, (v, neighbor))
    return dist

def main():
    n, s, t, q = map(int, input().split())
    hills = [tuple(map(int, input().split())) for _ in range(n)]
    springs = set(map(int, input().split()))
    towns = set(map(int, input().split()))
    graph = {i: {} for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if hills[i - 1][2] < hills[j - 1][2]:
                graph[i][j] = math.sqrt((hills[i - 1][0] - hills[j - 1][0]) ** 2 + (hills[i - 1][1] - hills[j - 1][1]) ** 2)
            elif hills[i - 1][2] > hills[j - 1][2]:
                graph[j][i] = math.sqrt((hills[j - 1][0] - hills[i - 1][0]) ** 2 + (hills[j - 1][1] - hills[i - 1][1]) ** 2)
    dist = dijkstra(graph, 1)
    total_length = 0
    for i in range(1, n + 1):
        if i in springs:
            total_length += dist[i]
    if total_length > q:
        print("IMPOSSIBLE")
    else:
        print(total_length)

if __name__ == '__main__':
    main()

