
def is_tree(n, d, k):
    # Check if the input is valid
    if n < 1 or d < 1 or k < 1:
        return False
    
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n)]
    
    # Add edges to the graph
    for i in range(n - 1):
        for j in range(i + 1, n):
            if j - i <= d and len(graph[i]) < k and len(graph[j]) < k:
                graph[i].append(j)
                graph[j].append(i)
    
    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # Check if all vertices are reachable from the first vertex
    for i in range(1, n):
        if not visited[i]:
            return False
    
    return True

