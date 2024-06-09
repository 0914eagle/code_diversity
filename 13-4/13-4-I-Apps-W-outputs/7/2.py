
def solve(n, m, routes, prices):
    # Initialize a dictionary to store the minimum cost to visit each city
    min_cost = {i: float('inf') for i in range(1, n + 1)}
    min_cost[1] = 0
    
    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route from city i
        for route in routes:
            # If the route starts in city i, update the minimum cost to visit city j
            if route[0] == i:
                j = route[1]
                cost = route[2] + min_cost[j]
                min_cost[i] = min(min_cost[i], cost)
    
    # Loop through each city
    for i in range(1, n + 1):
        # Add the cost of attending the concert in city i
        min_cost[i] += prices[i - 1]
    
    return min_cost

