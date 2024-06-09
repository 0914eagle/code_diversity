
def solve(n, m, routes, prices):
    # Initialize a dictionary to store the minimum cost to visit each city
    min_cost = {i: float('inf') for i in range(1, n + 1)}
    min_cost[1] = 0
    
    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route
        for j in range(m):
            # Get the city at the end of the route
            city = routes[j][1] if routes[j][0] == i else routes[j][0]
            # If the city has not been visited yet, update the minimum cost
            if min_cost[city] > min_cost[i] + routes[j][2]:
                min_cost[city] = min_cost[i] + routes[j][2]
    
    # Return the minimum cost to visit each city
    return [min_cost[i] + prices[i - 1] for i in range(1, n + 1)]

