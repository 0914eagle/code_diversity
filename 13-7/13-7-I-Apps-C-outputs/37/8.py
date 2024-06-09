
def solve(G, K, R, roads, gigs):
    # Initialize a graph with the given number of vertices and edges
    graph = [[] for _ in range(K + 1)]
    for (u, v, w) in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Initialize the minimum time and maximum profit for each vertex
    min_time = [float('inf') for _ in range(K + 1)]
    max_profit = [0 for _ in range(K + 1)]
    min_time[1] = 0
    
    # Perform a breadth-first search from vertex 1 to find the minimum time and maximum profit for each vertex
    queue = [(1, 0)]
    while queue:
        (vertex, time) = queue.pop(0)
        for (neighbor, weight) in graph[vertex]:
            if time + weight < min_time[neighbor]:
                min_time[neighbor] = time + weight
                max_profit[neighbor] = max(max_profit[neighbor], max_profit[vertex])
                queue.append((neighbor, min_time[neighbor]))
    
    # Find the maximum profit by considering all possible combinations of gigs
    max_profit = 0
    for i in range(G):
        (vertex, start, end, profit) = gigs[i]
        if min_time[vertex] <= start and end <= min_time[1]:
            max_profit = max(max_profit, profit + max_profit[vertex])
    
    return max_profit

