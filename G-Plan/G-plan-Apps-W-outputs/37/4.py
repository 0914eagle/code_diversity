ulate_rebuilds(n, m, roads, k, path):
    graph = {}
    for u, v in roads:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    queue = [path[0]]
    rebuilds = 0
    for i in range(1, k):
        current = path[i]
        while queue:
            node = queue.pop(0)
            if node == current:
                queue.append(node)
                break
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in path[i:]:
                        queue.append(neighbor)
                rebuilds += 1

    return rebuilds, len(visited) - rebuilds

if __name__ == "__main__":
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    min_rebuilds, max_rebuilds = calculate_rebuilds(n, m, roads, k, path)
    print(min_rebuilds, max_rebuilds)
