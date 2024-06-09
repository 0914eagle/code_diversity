
def get_maximum_water_reach(n, p, k, pipes, improvements):
    # Initialize the graph with the given pipes
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for pipe in pipes:
        graph[pipe[0]].append((pipe[1], pipe[2]))
    
    # Initialize the maximum water reach for each station
    max_water_reach = [0] * (n+1)
    max_water_reach[1] = 1000
    
    # Iterate through the improvements
    for improvement in improvements:
        # Get the current capacity of the pipe
        current_capacity = 0
        if improvement[0] in graph and improvement[1] in graph[improvement[0]]:
            current_capacity = graph[improvement[0]][graph[improvement[0]].index(improvement[1])][1]
        
        # Increase the capacity of the pipe
        graph[improvement[0]][graph[improvement[0]].index(improvement[1])] = (improvement[1], current_capacity + improvement[2])
        
        # Update the maximum water reach for each station
        for station in graph:
            for neighbor, capacity in graph[station]:
                max_water_reach[neighbor] = max(max_water_reach[neighbor], max_water_reach[station] - capacity)
    
    # Return the maximum water reach for the mansion
    return max_water_reach[-1]

