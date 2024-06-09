
def solve(n, d, a, m, fares):
    # Initialize a dictionary to store the minimum cost to reach each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0

    # Loop through each city in the tour schedule
    for i in range(d):
        current_city = a[i]
        next_city = a[i + 1]

        # Loop through each airfare
        for s, d, t, p in fares:
            # Check if the airfare is valid for the current city and the next city
            if s == current_city and d == next_city:
                # If the airfare is a round trip ticket, add the cost to the minimum cost for the next city
                if t == 'R':
                    min_cost[next_city] = min(min_cost[next_city], min_cost[current_city] + p)
                # If the airfare is a one-way ticket, add the cost to the minimum cost for the current city
                elif t == 'O':
                    min_cost[current_city] = min(min_cost[current_city], min_cost[next_city] + p)

    # Return the minimum cost to reach the last city in the tour schedule
    return min_cost[a[-1]]

