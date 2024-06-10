
def min_time_to_reach_bed(n, m, s, t, tubes):
    graph = {i: [] for i in range(n)}
    for a, b, w in tubes:
        graph[a].append((b, w))

    dist = [float('inf')] * n
    dist[s] = 0

    queue = [s]
    while queue:
        current = queue.pop(0)
        for neighbor, weight in graph[current]:
            if dist[current] + weight < dist[neighbor]:
                dist[neighbor] = dist[current] + weight
                queue.append(neighbor)

    return dist[t] if dist[t] != float('inf') else 'infinity'


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [list(map(int, input().split())) for _ in range(m)]
    print(min_time_to_reach_bed(n, m, s, t, tubes))
