
def solve(n, d, a, m, s, d, t, p):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0
    
    # Loop through each airfare
    for i in range(m):
        # If the airfare is a round trip ticket, add the cost to both the origin and destination cities
        if t[i] == 'R':
            min_cost[s[i]] = min(min_cost[s[i]], p[i])
            min_cost[d[i]] = min(min_cost[d[i]], p[i])
        # If the airfare is a one-way ticket, add the cost to the origin city only
        else:
            min_cost[s[i]] = min(min_cost[s[i]], p[i])
    
    # Loop through each city in the tour schedule
    for i in range(d):
        # If the current city is not the last city in the tour, find the minimum cost to get to the next city
        if i != d - 1:
            min_cost[a[i + 1]] = min(min_cost[a[i + 1]], min_cost[a[i]] + p[i])
    
    # Return the minimum cost to complete the tour
    return min_cost[a[-1]]

