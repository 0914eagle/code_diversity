
def solve(n, d, schedule, airfares):
    # Initialize a dictionary to store the minimum cost for each city
    min_cost = {city: float('inf') for city in range(1, n + 1)}
    min_cost[schedule[0]] = 0
    
    # Loop through each airfare
    for s, d, t, p in airfares:
        # If the airfare is a round trip ticket and the destination city is the same as the origin city, skip it
        if t == 'R' and s == d:
            continue
        
        # If the airfare is a one-way ticket and the destination city is not the same as the origin city, skip it
        if t == 'O' and s != d:
            continue
        
        # If the airfare is a round trip ticket and the destination city is not the same as the origin city, update the minimum cost for the destination city
        if t == 'R' and s != d:
            min_cost[d] = min(min_cost[d], min_cost[s] + p)
        
        # If the airfare is a one-way ticket and the destination city is not the same as the origin city, update the minimum cost for the destination city
        if t == 'O' and s != d:
            min_cost[d] = min(min_cost[d], min_cost[s] + p)
    
    # Return the minimum cost for the last city in the schedule
    return min_cost[schedule[-1]]

