
def get_maximum_gold(n, m, roads, gold):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[roads[i][0] - 1].append(roads[i][1] - 1)
        graph[roads[i][1] - 1].append(roads[i][0] - 1)
    
    # Initialize the maximum gold to be 0
    max_gold = 0
    
    # Iterate through all possible paths from the bandit's home to the king's castle
    for path in all_paths(graph, 0, n - 1):
        # Initialize the gold collected on this path to be 0
        gold_collected = 0
        
        # Iterate through the villages in the path
        for i in range(len(path) - 1):
            # Add the gold in the current village to the total gold collected
            gold_collected += gold[path[i]]
            
            # If the current village is not the bandit's home and the next village is not the king's castle,
            # then the bandits can steal the gold in the current village
            if path[i] != 0 and path[i + 1] != n - 1:
                gold_collected += gold[path[i]]
        
        # Update the maximum gold if the gold collected on this path is greater than the current maximum gold
        max_gold = max(max_gold, gold_collected)
    
    return max_gold

def all_paths(graph, start, end):
    # Base case: if the start and end vertices are the same, return the path
    if start == end:
        yield [start]
    
    # Recursive case: generate all paths from the start vertex and extend them by adding the start vertex
    for path in all_paths(graph, start, end):
        yield [start] + path
    
    # Recursive case: generate all paths from the adjacent vertices and extend them by adding the start vertex
    for adjacent in graph[start]:
        for path in all_paths(graph, adjacent, end):
            yield [start] + path

