
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
            # Perform DFS on the graph starting from the current village
            dfs(graph, visited, parent, village)
            # Get the maximum gold collected by the bandits during the DFS
            max_gold = max(max_gold, get_max_gold(parent, village, gold))
    
    return max_gold

def dfs(graph, visited, parent, current_village):
    # Mark the current village as visited
    visited[current_village] = True
    # Iterate through the neighbors of the current village
    for neighbor in graph[current_village]:
        # If the neighbor has not been visited yet
        if not visited[neighbor]:
            # Perform DFS on the neighbor
            dfs(graph, visited, parent, neighbor)
            # Update the parent of the current village
            parent[current_village] = neighbor
            break

def get_max_gold(parent, current_village, gold):
    # Initialize the maximum gold to 0
    max_gold = 0
    # Iterate through the parents of the current village
    while current_village != 0:
        # Add the gold in the current village to the maximum gold
        max_gold += gold[current_village]
        # Update the current village to its parent
        current_village = parent[current_village]
    
    return max_gold

# Test the function with the given examples
assert get_maximum_gold(3, 3, [[1, 2], [2, 3], [1, 3]], [1, 1, 2]) == 0
assert get_maximum_gold(4, 4, [[1, 3], [1, 4], [2, 3], [2, 4]], [24, 10, 10, 10]) == 24
assert get_maximum_gold(6, 8, [[1, 3], [1, 4], [3, 6], [4, 5], [3, 5], [4, 6], [2, 5], [2, 6]], [100, 500, 300, 75, 75, 75, 75, 75]) == 800

