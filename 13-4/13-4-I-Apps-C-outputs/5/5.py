
def solve(n, d, a, m, s, d, t, p):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[a[0]] = 0
    
    # Loop through each airfare
    for i in range(m):
        # Check if the airfare is a one-way ticket
        if t[i] == 'O':
            # If the airfare is a one-way ticket, check if the origin city is the same as the previous city
            if s[i] == d[i - 1]:
                # If the origin city is the same as the previous city, update the minimum cost for the destination city
                min_cost[d[i]] = min(min_cost[d[i]], min_cost[s[i]] + p[i])
        else:
            # If the airfare is a round trip ticket, check if the origin city is the same as the previous city
            if s[i] == d[i - 1]:
                # If the origin city is the same as the previous city, update the minimum cost for the destination city
                min_cost[d[i]] = min(min_cost[d[i]], min_cost[s[i]] + p[i])
            # Check if the destination city is the same as the next city
            if d[i] == s[i + 1]:
                # If the destination city is the same as the next city, update the minimum cost for the origin city
                min_cost[s[i]] = min(min_cost[s[i]], min_cost[d[i]] + p[i])
    
    # Return the minimum cost for the last city
    return min_cost[a[-1]]

