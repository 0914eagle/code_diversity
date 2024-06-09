
def solve(n, d, a, m, fares):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0

    # Loop through each airfare
    for s, d, t, p in fares:
        # If the ticket is a round trip ticket and the cost is less than the current minimum cost, update the minimum cost
        if t == 'R' and min_cost[s] + p < min_cost[d]:
            min_cost[d] = min_cost[s] + p

    # Loop through each city in the tour
    for i in range(d - 1):
        # If the cost of traveling from the current city to the next city is less than the current minimum cost, update the minimum cost
        if min_cost[a[i]] + min_cost[a[i + 1]] < min_cost[a[i + 1]]:
            min_cost[a[i + 1]] = min_cost[a[i]] + min_cost[a[i + 1]]

    # Return the minimum cost for the last city
    return min_cost[a[-1]]

