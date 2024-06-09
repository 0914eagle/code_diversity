
def solve(n, m, routes, prices):
    # Initialize a dictionary to store the minimum cost to visit each city
    min_cost = {i: float('inf') for i in range(1, n + 1)}
    min_cost[1] = 0
    
    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route from city i
        for j in range(m):
            # If the route is from city i to some other city j
            if routes[j][0] == i:
                # Calculate the minimum cost to visit city j and return to city i
                cost = min_cost[i] + routes[j][2] + prices[routes[j][1]]
                # If the minimum cost to visit city j is less than the current minimum cost, update the minimum cost
                if cost < min_cost[routes[j][1]]:
                    min_cost[routes[j][1]] = cost
    
    return [min_cost[i] for i in range(1, n + 1)]

