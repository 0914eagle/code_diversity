
def solve(n, m, routes, prices):
    # Initialize a dictionary to store the minimum cost to reach each city
    dp = {i: float('inf') for i in range(1, n + 1)}
    dp[1] = 0

    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route from the current city
        for j in range(m):
            # If the route is from the current city to another city
            if routes[j][0] == i:
                # Calculate the minimum cost to reach the other city
                cost = dp[i] + routes[j][2]
                # If the minimum cost is less than the current minimum cost, update the minimum cost
                if cost < dp[routes[j][1]]:
                    dp[routes[j][1]] = cost

    # Loop through each city
    for i in range(1, n + 1):
        # Add the cost of the concert to the minimum cost to reach the city
        dp[i] += prices[i - 1]

    return dp

