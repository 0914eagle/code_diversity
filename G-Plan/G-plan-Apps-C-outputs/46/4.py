
def min_time_to_reach_bed(n, m, s, t, tubes):
    graph = {}
    for a, b, w in tubes:
        if a not in graph:
            graph[a] = []
        graph[a].append((b, w))

    visited = set()
    left_time = [float('inf')] * n
    right_time = [float('inf')] * n

    left_time[s] = 0
    right_time[s] = 0

    queue = [(s, 0)]
    while queue:
        current, time = queue.pop(0)
        visited.add(current)

        if current in graph:
            for neighbor, weight in graph[current]:
                if time % 2 == 0:  # Left hemisphere's turn
                    if time + weight < left_time[neighbor]:
                        left_time[neighbor] = time + weight
                        if neighbor not in visited:
                            queue.append((neighbor, time + weight))
                else:  # Right hemisphere's turn
                    if time + weight < right_time[neighbor]:
                        right_time[neighbor] = time + weight
                        if neighbor not in visited:
                            queue.append((neighbor, time + weight))

    return left_time[t] if left_time[t] < float('inf') else "infinity"

if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    tubes = [list(map(int, input().split())) for _ in range(m)]
    print(min_time_to_reach_bed(n, m, s, t, tubes))
