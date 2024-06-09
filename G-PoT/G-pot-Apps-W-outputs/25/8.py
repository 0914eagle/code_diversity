
def max_color_changes(N, M, edges):
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    colors = [0] * N
    queue = [(0, 0)]  # (node, color)
    visited = set()
    
    while queue:
        node, color = queue.pop(0)
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                colors[neighbor] = 1 - color
                queue.append((neighbor, 1 - color))
    
    color_changes = sum(1 for a, b in edges if colors[a-1] != colors[b-1])
    
    return color_changes

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate and print output
print(max_color_changes(N, M, edges))
