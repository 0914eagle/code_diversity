
def get_min_cost(n, m, roads):
    # Initialize the cost array with -1 for all areas
    cost = [-1] * (n + 1)
    cost[1] = 0
    
    # Loop through each road
    for i in range(m):
        # Get the two areas connected by the road
        area1, area2 = roads[i][0], roads[i][1]
        
        # If the cost of area1 is not yet known, set it to the cost of area2 + 1
        if cost[area1] == -1:
            cost[area1] = cost[area2] + 1
        
        # If the cost of area2 is not yet known, set it to the cost of area1 + 1
        if cost[area2] == -1:
            cost[area2] = cost[area1] + 1
    
    # Loop through each area and check if the cost is valid
    for i in range(1, n + 1):
        # If the cost is not valid, return -1
        if (cost[i] + cost[i - 1]) % 3 == 1:
            return -1
    
    # If all costs are valid, return the minimum cost
    return min(cost)

