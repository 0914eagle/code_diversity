
def min_time_to_reach_bed(n, m, s, t, tubes):
    graph = {i: [] for i in range(n)}
    for a, b, w in tubes:
        graph[a].append((b, w))

    visited = [False] * n
    left_time = [float('inf')] * n
    right_time = [float('inf')] * n

    left_time[s] = 0
    right_time[s] = 0

    queue = [(s, True)]
    while queue:
        current, is_left = queue.pop(0)
        visited[current] = True

        for neighbor, weight in graph[current]:
            if is_left:
                if left_time[current] + weight < right_time[neighbor]:
                    right_time[neighbor] = left_time[current] + weight
                    if not visited[neighbor]:
                        queue.append((neighbor, False))
            else:
                if right_time[current] + weight < left_time[neighbor]:
                    left_time[neighbor] = right_time[current] + weight
                    if not visited[neighbor]:
                        queue.append((neighbor, True))

    return left_time[t] if left_time[t] != float('inf') else "infinity"


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [tuple(map(int, input().split())) for _ in range(m)]

    result = min_time_to_reach_bed(n, m, s, t, tubes)
    print(result)
