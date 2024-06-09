
def max_color_changes(N, M, edges):
    graph = {i: [] for i in range(1, N+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    color_changes = 0
    for node in graph[1]:
        if len(set(graph[node])) == 2:
            color_changes += 1
    
    return color_changes

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Output the result
print(max_color_changes(N, M, edges))
