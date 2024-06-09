
def solve(n, d, a, m, fares):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0

    # Loop through each airfare
    for s, d, t, p in fares:
        # If the airfare is a round trip ticket, add the cost to both the origin and destination cities
        if t == 'R':
            min_cost[s] = min(min_cost[s], p)
            min_cost[d] = min(min_cost[d], p)
        # If the airfare is a one-way ticket, add the cost to the origin city only
        else:
            min_cost[s] = min(min_cost[s], p)

    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(d - 1):
        total_cost += min_cost[a[i]]

    return total_cost

