
def get_maximum_gold(n, m, roads, gold):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize a dictionary to store the maximum gold that can be stolen from each village
    max_gold = {1: 0}
    
    # Iterate through each village and calculate the maximum gold that can be stolen from it
    for i in range(2, n + 1):
        max_gold[i] = max(max_gold[j] + gold[i] for j in graph[i])
    
    # Return the maximum gold that can be stolen from the bandit's home
    return max_gold[1]

