
def solve(n, d, a, m, fares):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0

    # Loop through each airfare
    for s, d, t, p in fares:
        # If the ticket is a one-way ticket and the cost is less than the current minimum cost, update the minimum cost
        if t == 'O' and p < min_cost[s]:
            min_cost[s] = p

        # If the ticket is a round-trip ticket and the cost is less than the current minimum cost for both the origin and destination cities, update the minimum cost
        if t == 'R' and p < min_cost[s] and p < min_cost[d]:
            min_cost[s] = p
            min_cost[d] = p

    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(d - 1):
        total_cost += min_cost[a[i]]

    return total_cost

