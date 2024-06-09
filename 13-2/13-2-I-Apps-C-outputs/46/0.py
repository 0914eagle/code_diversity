
def get_maximum_gold(n, m, roads, gold):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        graph[roads[i][0]].append(roads[i][1])
        graph[roads[i][1]].append(roads[i][0])
    
    # Initialize a visited array and a parent array
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    
    # Initialize the maximum gold to 0
    max_gold = 0
    
    # Iterate through all the villages
    for village in range(1, n + 1):
        # If the village has not been visited yet
        if not visited[village]:
            # Perform DFS to find the maximum gold that can be stolen
            max_gold = max(max_gold, dfs(graph, visited, parent, village, gold))
    
    return max_gold

def dfs(graph, visited, parent, village, gold):
    # Mark the current village as visited
    visited[village] = True
    parent[village] = 1
    
    # Initialize the maximum gold to 0
    max_gold = 0
    
    # Iterate through the neighbors of the current village
    for neighbor in graph[village]:
        # If the neighbor has not been visited yet
        if not visited[neighbor]:
            # Perform DFS on the neighbor
            max_gold = max(max_gold, dfs(graph, visited, parent, neighbor, gold))
    
    # Return the maximum gold that can be stolen from the current village
    return max_gold + gold[village]

