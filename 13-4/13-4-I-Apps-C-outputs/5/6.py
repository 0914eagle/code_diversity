
def solve(n, d, a, m, s, d, t, p):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0

    # Loop through each airfare
    for i in range(m):
        # Check if the airfare is for a round trip ticket
        if t[i] == 'R':
            # Update the minimum cost for the origin and destination cities
            min_cost[s[i]] = min(min_cost[s[i]], p[i])
            min_cost[d[i]] = min(min_cost[d[i]], p[i])
        else:
            # Update the minimum cost for the origin city
            min_cost[s[i]] = min(min_cost[s[i]], p[i])

    # Loop through each city in the tour
    for i in range(d):
        # Check if the current city is the same as the previous city
        if a[i] == a[i - 1]:
            # If so, skip this city
            continue
        # Update the minimum cost for the current city
        min_cost[a[i]] = min(min_cost[a[i]], min_cost[a[i - 1]] + p[i - 1])

    # Return the minimum cost for the last city
    return min_cost[a[-1]]

