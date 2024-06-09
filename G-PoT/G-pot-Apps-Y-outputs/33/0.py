
def min_extra_roads(n, m, s, roads):
    graph = {i: [] for i in range(1, n+1)}
    for u, v in roads:
        graph[u].append(v)
    
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    
    visited = set()
    dfs(s, visited)
    
    extra_roads = 0
    for city in range(1, n+1):
        if city != s and city not in visited:
            extra_roads += 1
    
    return extra_roads

# Input parsing
n, m, s = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_extra_roads(n, m, s, roads))
