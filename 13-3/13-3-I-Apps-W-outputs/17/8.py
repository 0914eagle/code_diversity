
def solve(n, m, a):
    # Initialize the graph with the given weights
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i].append((a[i - 1] + a[j - 1], j))
    
    # Sort the edges in non-decreasing order based on their weight
    for i in range(1, n + 1):
        graph[i].sort(key=lambda x: x[0])
    
    # Initialize the minimum spanning tree with the first edge
    mst = [(1, 2, a[0])]
    visited = [False] * (n + 1)
    visited[1] = True
    
    # Loop through the remaining edges and add them to the MST
    for i in range(2, n):
        # Find the edge with the minimum weight that connects a visited node to an unvisited node
        min_weight = float("inf")
        min_edge = None
        for j in range(1, n + 1):
            if not visited[j]:
                for edge in graph[j]:
                    if visited[edge[1]]:
                        if edge[0] < min_weight:
                            min_weight = edge[0]
                            min_edge = (j, edge[1], edge[0])
                            break
        
        # Add the minimum edge to the MST and mark the nodes as visited
        mst.append(min_edge)
        visited[min_edge[0]] = True
        visited[min_edge[1]] = True
    
    # Check if the MST has exactly m - 1 edges
    if len(mst) != m:
        return -1
    
    # Return the total cost of the MST
    return sum(edge[2] for edge in mst)

