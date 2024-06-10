max_rebuilds(n, m, roads, k, path):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start, end):
        visited = set()
        queue = [(start, 0)]
        rebuilds = 0

        while queue:
            node, dist = queue.pop(0)
            visited.add(node)

            if node == end:
                return rebuilds

            for neighbor in graph[node]:
                if neighbor not in path:
                    rebuilds += 1
                    queue.append((neighbor, dist + 1))
                else:
                    queue.append((neighbor, dist))

        return rebuilds

    min_rebuilds = bfs(path[0], path[-1])
    max_rebuilds = sum(1 for node in path[1:-1] if len(graph[node]) > 1)

    return min_rebuilds, max_rebuilds


if __name__ == "__main__":
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    min_rebuilds, max_rebuilds = min_max_rebuilds(n, m, roads, k, path)
    print(min_rebuilds, max_rebuilds)
""