
def solve(n, m, routes, a):
    # Initialize a dictionary to store the minimum cost to visit each city
    dp = {i: float('inf') for i in range(1, n + 1)}
    dp[1] = 0

    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route
        for j in range(m):
            # Get the cost of the route
            cost = routes[j][2]
            # Get the cities involved in the route
            v, u = routes[j][0], routes[j][1]
            # If the current city is the starting city or the destination city, add the cost of the route to the minimum cost
            if i == v or i == u:
                dp[i] = min(dp[i], dp[v] + cost + a[u])
            # If the current city is between the starting and destination cities, add the cost of the route to the minimum cost
            elif i != v and i != u:
                dp[i] = min(dp[i], dp[v] + cost + dp[u])

    return [int(dp[i]) for i in range(1, n + 1)]

