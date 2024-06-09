
def solve(n, d, a, m, s, d, t, p):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0
    
    # Loop through each airfare
    for i in range(m):
        # Check if the airfare is a round trip ticket
        if t[i] == 'R':
            # Update the minimum cost for the destination city
            min_cost[d[i]] = min(min_cost[d[i]], min_cost[s[i]] + p[i])
        else:
            # Update the minimum cost for the destination city
            min_cost[d[i]] = min(min_cost[d[i]], min_cost[s[i]] + p[i] / 2)
    
    # Return the minimum cost for the last city
    return min_cost[a[-1]]

