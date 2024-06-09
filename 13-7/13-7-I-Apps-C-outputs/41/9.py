
def get_maximum_gold(n, m, roads, villages):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[roads[i][0] - 1].append(roads[i][1] - 1)
        graph[roads[i][1] - 1].append(roads[i][0] - 1)
    
    # Initialize the maximum gold to 0
    max_gold = 0
    
    # Iterate through all possible paths from the bandit's home to the king's castle
    for path in all_paths(graph, 0, 1):
        # Initialize the gold collected on this path to 0
        gold = 0
        
        # Iterate through the villages in the path
        for i in range(len(path) - 1):
            # If the current village is not the bandit's home, add its gold to the total gold collected
            if path[i] != 0:
                gold += villages[path[i] - 1]
        
        # If the total gold collected on this path is greater than the current maximum gold, update the maximum gold
        if gold > max_gold:
            max_gold = gold
    
    # Return the maximum gold collected
    return max_gold

# Function to find all paths between two nodes in a graph
def all_paths(graph, start, end):
    # Initialize the path as a list containing only the start node
    path = [start]
    
    # If the start node is the same as the end node, return the path
    if start == end:
        yield path
    
    # Iterate through the neighbors of the start node
    for neighbor in graph[start]:
        # If the neighbor has not been visited, recurse with the neighbor as the new start node
        if neighbor not in path:
            for new_path in all_paths(graph, neighbor, end):
                yield path + new_path

# Test the function with a sample input
n = 6
m = 8
roads = [[1, 3], [1, 4], [3, 6], [4, 5], [3, 5], [4, 6], [2, 5], [2, 6]]
villages = [100, 500, 300, 75]
print(get_maximum_gold(n, m, roads, villages))

