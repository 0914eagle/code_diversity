
def shortest_path_bfs(n, m, s, t, tubes):
    graph = {i: [] for i in range(n)}
    for a, b, w in tubes:
        graph[a].append((b, w))

    visited = [False] * n
    distances = [float('inf')] * n
    distances[s] = 0

    queue = [s]
    while queue:
        current = queue.pop(0)
        visited[current] = True

        for neighbor, weight in graph[current]:
            if distances[current] + weight < distances[neighbor]:
                distances[neighbor] = distances[current] + weight
                if not visited[neighbor]:
                    queue.append(neighbor)

    return distances[t] if distances[t] != float('inf') else 'infinity'


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [list(map(int, input().split())) for _ in range(m)]
    print(shortest_path_bfs(n, m, s, t, tubes))
