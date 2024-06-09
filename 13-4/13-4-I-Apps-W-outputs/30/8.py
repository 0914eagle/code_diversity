
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
    
    # Create a graph representing the road network
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
    if len(edges) != n-1:
        return "NO"
    
    # The graph is a tree, so we can find a Eulerian circuit
    circuit = []
    node = 0
    while node != 0:
        circuit.append(node+1)
        node = graph[node].pop(0)
    
    # Redirect the roads to make the road network tourist-friendly
    redirected_edges = []
    for i in range(n):
        a, b = circuit[i-1], circuit[i]
        if a != b:
            redirected_edges.append([a, b])
    
    return "YES\n" + "\n".join(map(str, redirected_edges))

