
def max_color_changes(N, M, edges):
    graph = {i: [] for i in range(1, N+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    color_changes = 0
    for node in range(1, N+1):
        for neighbor in graph[node]:
            if node < neighbor and (node, neighbor) not in edges:
                color_changes += 1
    
    return color_changes

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the output
print(max_color_changes(N, M, edges))
