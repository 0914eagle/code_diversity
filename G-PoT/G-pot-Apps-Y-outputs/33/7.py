
def min_extra_roads(n, m, s, roads):
    graph = {i: set() for i in range(1, n+1)}
    for u, v in roads:
        graph[u].add(v)

    visited = set()
    stack = [s]
    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    extra_roads = 0
    for city in range(1, n+1):
        if city != s and city not in visited:
            extra_roads += 1

    return extra_roads

n, m, s = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

result = min_extra_roads(n, m, s, roads)
print(result)
