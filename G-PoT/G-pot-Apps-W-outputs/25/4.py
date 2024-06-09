
def max_color_changes(N, M, edges):
    graph = {i: [] for i in range(1, N+1)}
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    
    color_changes = 0
    for node in range(1, N+1):
        for neighbor in graph[node]:
            if neighbor < node:
                continue
            if (node + neighbor) % 2 == 0:
                color_changes += 1
    
    return color_changes

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate and output the maximum number of color changes
print(max_color_changes(N, M, edges))
