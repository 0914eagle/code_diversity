
def max_color_changes(N, M, edges):
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    colors = [-1] * N
    colors[0] = 0
    
    stack = [0]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                colors[neighbor] = 1 - colors[node]
                stack.append(neighbor)
    
    red_edges = sum(1 for a, b in edges if colors[a-1] != colors[b-1])
    return min(red_edges, M - red_edges)

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
print(max_color_changes(N, M, edges))
