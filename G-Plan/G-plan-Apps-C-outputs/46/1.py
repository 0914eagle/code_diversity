
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
    visited[s] = True

    while queue:
        current, current_time = queue.pop(0)
        for neighbor, weight in graph[current]:
            new_time = current_time + weight
            if current_time % 2 == 0:  # Left hemisphere's turn
                if new_time < left_time[neighbor]:
                    left_time[neighbor] = new_time
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, new_time))
            else:  # Right hemisphere's turn
                if new_time < right_time[neighbor]:
                    right_time[neighbor] = new_time
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, new_time))

    if left_time[t] == float('inf') or right_time[t] == float('inf'):
        return "infinity"
    return left_time[t]

if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [tuple(map(int, input().split())) for _ in range(m)]
    print(min_time_to_reach_bed(n, m, s, t, tubes))
