
def max_color_changes(N, M, edges):
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    color_changes = 0
    for i in range(N):
        for neighbor in graph[i]:
            if neighbor > i:
                color_changes += 1
    
    return color_changes // 2

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and output the result
print(max_color_changes(N, M, edges))
