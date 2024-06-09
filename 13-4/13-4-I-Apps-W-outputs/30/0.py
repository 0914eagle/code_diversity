
def solve_mancunia(n, e, edges):
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
    
    # Create a graph to represent the road network
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
    
    # Check if the graph is connected
    visited = [False] * (n + 1)
    queue = [1]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            queue += graph[node]
    
    if not all(visited):
        return "NO"
    
    # Check if the graph is a tree
    if len(edges) != n - 1:
        return "NO"
    
    # Check if the graph is a Hamiltonian cycle
    for node in range(1, n + 1):
        if not visited[node]:
            return "NO"
    
    # If all conditions are met, return the Hamiltonian cycle
    return "YES"
    cycle = []
    node = 1
    while node != 1:
        cycle.append(node)
        node = graph[node][0]
    return cycle

