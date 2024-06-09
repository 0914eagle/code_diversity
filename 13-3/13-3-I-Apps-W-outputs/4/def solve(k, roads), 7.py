
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))
    
    # Find the minimum sum by performing a depth-first search and keeping track of the minimum distance from each node to the starting node
    min_dist = {1: 0}
    for i in range(2, 2*k+1):
        min_dist[i] = float('inf')
    for i in range(1, 2*k+1):
        for j, t in graph[i]:
            min_dist[j] = min(min_dist[j], min_dist[i] + t)
    
    # Find the maximum sum by performing a breadth-first search and keeping track of the maximum distance from each node to the starting node
    max_dist = {1: 0}
    for i in range(2, 2*k+1):
        max_dist[i] = float('-inf')
    for i in range(1, 2*k+1):
        for j, t in graph[i]:
            max_dist[j] = max(max_dist[j], max_dist[i] + t)
    
    return min_dist[2*k], max_dist[2*k]

