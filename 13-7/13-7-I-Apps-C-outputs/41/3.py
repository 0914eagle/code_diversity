
def get_maximum_gold(n, m, gold, roads):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)
    
    # Initialize a list to store the maximum gold that can be stolen from each village
    max_gold = [0] * (n + 1)
    max_gold[1] = gold[0]
    
    # Iterate through each village in the graph
    for village in range(1, n + 1):
        # If the village is not the bandit's home, check if there is a path from the village to the king's castle
        if village != 1 and 2 in graph[village]:
            # If there is a path, update the maximum gold that can be stolen from the village
            max_gold[village] = max(max_gold[village], max_gold[village - 1] + gold[village - 1])
    
    # Return the maximum gold that can be stolen from the bandit's home and still be able to return home safely
    return max_gold[n]

