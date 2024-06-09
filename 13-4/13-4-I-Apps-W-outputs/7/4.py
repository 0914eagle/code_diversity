
def solve(n, m, routes, prices):
    # Initialize a dictionary to store the minimum cost to reach each city
    min_cost = {i: float('inf') for i in range(1, n + 1)}
    min_cost[1] = 0
    
    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route
        for route in routes:
            # Check if the route starts in city i
            if route[0] == i:
                # Calculate the minimum cost to reach the destination city
                dest_cost = min_cost[i] + route[2]
                # Check if the minimum cost to reach the destination city is less than the current minimum cost
                if dest_cost < min_cost[route[1]]:
                    # Update the minimum cost to reach the destination city
                    min_cost[route[1]] = dest_cost
    
    # Loop through each city
    for i in range(1, n + 1):
        # Calculate the total cost to visit the city, including the concert ticket price
        total_cost = min_cost[i] + prices[i - 1]
        # Check if the total cost is less than the current minimum cost
        if total_cost < min_cost[i]:
            # Update the minimum cost to visit the city
            min_cost[i] = total_cost
    
    # Return the minimum cost to visit each city
    return [min_cost[i] for i in range(1, n + 1)]

