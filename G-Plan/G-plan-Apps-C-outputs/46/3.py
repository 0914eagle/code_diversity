
def min_time_to_reach_bed(n, m, s, t, tubes):
    graph = {i: [] for i in range(n)}
    for a, b, w in tubes:
        graph[a].append((b, w))

    dist = [float('inf')] * n
    dist[s] = 0

    q = [(0, s)]
    while q:
        time, node = q.pop(0)
        if node == t:
            return time

        for neighbor, weight in graph[node]:
            new_time = time + weight
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                q.append((new_time, neighbor))

    return "infinity"


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [list(map(int, input().split())) for _ in range(m)]
    print(min_time_to_reach_bed(n, m, s, t, tubes))
