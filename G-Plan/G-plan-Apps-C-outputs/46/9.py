
def min_time_to_reach_bed(n, m, s, t, tubes):
    graph = {i: [] for i in range(n)}
    for a, b, w in tubes:
        graph[a].append((b, w))

    visited = [False] * n
    left_time = [float('inf')] * n
    right_time = [float('inf')] * n

    left_time[s] = 0
    right_time[s] = 0

    queue = [(s, 0)]
    while queue:
        current, time = queue.pop(0)
        visited[current] = True

        for neighbor, weight in graph[current]:
            if not visited[neighbor] and time % 2 == 0:
                if left_time[current] + weight < left_time[neighbor]:
                    left_time[neighbor] = left_time[current] + weight
                    queue.append((neighbor, time + 1))
            elif not visited[neighbor] and time % 2 == 1:
                if right_time[current] + weight < right_time[neighbor]:
                    right_time[neighbor] = right_time[current] + weight
                    queue.append((neighbor, time + 1))

    return left_time[t] if left_time[t] < float('inf') else 'infinity'


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [list(map(int, input().split())) for _ in range(m)]

    result = min_time_to_reach_bed(n, m, s, t, tubes)
    print(result)
