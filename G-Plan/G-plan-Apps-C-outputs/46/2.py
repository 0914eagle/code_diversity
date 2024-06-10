
def min_time_to_reach_bed(n, m, s, t, tubes):
    graph = {i: [] for i in range(n)}
    for a, b, w in tubes:
        graph[a].append((b, w))

    visited = [False] * n
    time_left = [float('inf')] * n
    time_right = [float('inf')] * n

    time_left[s] = 0
    time_right[s] = float('inf')

    queue = [(s, 0, True)]  # (ball, time, is_left)
    while queue:
        ball, time, is_left = queue.pop(0)
        visited[ball] = True

        for neighbor, w in graph[ball]:
            if is_left and time + w < time_right[neighbor]:
                time_right[neighbor] = time + w
                if not visited[neighbor]:
                    queue.append((neighbor, time + w, False))
            elif not is_left and time + w < time_left[neighbor]:
                time_left[neighbor] = time + w
                if not visited[neighbor]:
                    queue.append((neighbor, time + w, True))

    return time_left[t] if time_left[t] != float('inf') else "infinity"


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [list(map(int, input().split())) for _ in range(m)]
    print(min_time_to_reach_bed(n, m, s, t, tubes))
