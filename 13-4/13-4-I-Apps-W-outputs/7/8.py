
def solve(n, m, routes, a):
    # Initialize a dictionary to store the minimum cost to travel to each city
    d = {i: float('inf') for i in range(1, n + 1)}
    d[1] = 0

    # Loop through each city
    for i in range(1, n + 1):
        # Loop through each route
        for j in range(m):
            # Extract the route information
            v, u, w = routes[j]

            # Check if the current city is the starting city of the route
            if i == v:
                # If the current city is the starting city, check if the minimum cost to travel to the next city is less than the current minimum cost
                if d[u] > d[i] + w:
                    d[u] = d[i] + w

    # Loop through each city
    for i in range(1, n + 1):
        # Calculate the minimum cost to travel to the city, attend the concert, and return to the city
        d[i] += a[i - 1]

    return d

