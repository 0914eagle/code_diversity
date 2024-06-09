
def max_color_changes(N, M, edges):
    # Create a graph representation
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize color changes to 0
    color_changes = 0
    
    # Check if there are odd cycles in the graph
    for i in range(1, N+1):
        for neighbor in graph[i]:
            if i < neighbor:
                color_changes += 1
    
    return color_changes // 2

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the output
print(max_color_changes(N, M, edges))
