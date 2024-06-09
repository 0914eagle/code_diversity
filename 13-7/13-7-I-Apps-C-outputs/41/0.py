
def get_max_gold(n, m, roads, gold):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[roads[i][0] - 1].append(roads[i][1] - 1)
        graph[roads[i][1] - 1].append(roads[i][0] - 1)
    
    # Initialize a dictionary to store the maximum amount of gold that can be stolen from each village
    max_gold = {i: 0 for i in range(n)}
    
    # Initialize a queue to perform BFS
    queue = [0]
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a village from the queue
        village = queue.pop(0)
        
        # If the village is not the bandit's home, add its gold to the maximum amount of gold that can be stolen
        if village != 0:
            max_gold[village] += gold[village]
        
        # Enqueue the neighbors of the dequeued village
        for neighbor in graph[village]:
            if neighbor not in queue:
                queue.append(neighbor)
    
    # Return the maximum amount of gold that can be stolen
    return max(max_gold.values())

