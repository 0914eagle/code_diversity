
def solve(n, e, edges):
    # Check if the input data is valid
    if n < 1 or n > 100000:
        return "NO"
    if e < 1 or e > 200000:
        return "NO"
    for edge in edges:
        if len(edge) != 2:
            return "NO"
        a, b = edge
        if a < 1 or a > n or b < 1 or b > n:
            return "NO"
    
    # Initialize the graph with the given edges
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a-1].append(b-1)
    
    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    while queue:
        node = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        queue += graph[node]
    
    if not all(visited):
        return "NO"
    
    # Check if the graph is a tree
    if len(edges) != n - 1:
        return "NO"
    
    # Check if the graph is a Hamiltonian cycle
    for i in range(n):
        if not graph[i]:
            return "NO"
    
    # If all conditions are met, return the Hamiltonian cycle
    return "YES"
    cycle = []
    for i in range(n):
        if graph[i]:
            cycle.append(i+1)
            break
    for i in range(n-1):
        cycle.append(graph[cycle[i]-1][0]+1)
    return cycle

