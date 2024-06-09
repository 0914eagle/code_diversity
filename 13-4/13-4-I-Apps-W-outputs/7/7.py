
def solve(n, m, routes, prices):
    # Initialize a dictionary to store the minimum cost to visit each city
    min_cost = {i: float('inf') for i in range(1, n + 1)}
    min_cost[1] = 0
    
    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route from city i
        for j in range(m):
            # Get the cost of the route
            cost = routes[j][2]
            # Get the city at the end of the route
            city = routes[j][1] if i == routes[j][0] else routes[j][0]
            # If the cost is less than the current minimum cost, update the minimum cost
            if min_cost[i] + cost < min_cost[city]:
                min_cost[city] = min_cost[i] + cost
    
    # Loop through each city
    for i in range(1, n + 1):
        # Add the cost of attending the concert to the minimum cost
        min_cost[i] += prices[i - 1]
    
    return [min_cost[i] for i in range(1, n + 1)]

