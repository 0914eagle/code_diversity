
def solve(n, m, routes, a):
    # Initialize a dictionary to store the minimum cost to visit each city
    dp = {i: float('inf') for i in range(1, n + 1)}
    dp[1] = 0

    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route from the current city
        for j in range(m):
            # If the route is from the current city to another city
            if routes[j][0] == i:
                # Calculate the minimum cost to visit the next city
                cost = dp[i] + routes[j][2] + a[routes[j][1]]
                # Update the minimum cost if it's less than the current minimum
                if cost < dp[routes[j][1]]:
                    dp[routes[j][1]] = cost

    # Return the minimum cost for each city
    return [dp[i] for i in range(1, n + 1)]

