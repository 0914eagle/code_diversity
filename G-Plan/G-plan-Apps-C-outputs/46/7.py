
def min_time_to_reach_bed(n, m, s, t, tubes):
    graph = {i: [] for i in range(n)}
    for a, b, w in tubes:
        graph[a].append((b, w))

    visited = [False] * n
    time_left = [float('inf')] * n
    time_right = [float('inf')] * n

    time_left[s] = 0
    time_right[s] = float('inf')

    queue = [(s, 0, True)]
    while queue:
        ball, time, is_left = queue.pop(0)
        visited[ball] = True

        for next_ball, w in graph[ball]:
            new_time = time + w
            if is_left and new_time < time_right[next_ball]:
                time_right[next_ball] = new_time
                if not visited[next_ball]:
                    queue.append((next_ball, new_time, False))
            elif not is_left and new_time < time_left[next_ball]:
                time_left[next_ball] = new_time
                if not visited[next_ball]:
                    queue.append((next_ball, new_time, True))

    if time_right[t] == float('inf'):
        print("infinity")
    else:
        print(time_right[t])


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [list(map(int, input().split())) for _ in range(m)]
    min_time_to_reach_bed(n, m, s, t, tubes)
