
def solve(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness, max_cost = 0, 0
    
    # Loop through all possible combinations of flavors
    for flavors in combinations(range(k), n):
        # Calculate the tastiness and cost of the current combination
        tastiness, cost = 0, 0
        for i in range(n):
            tastiness += t[flavors[i]]
            cost += a
        for i in range(n-1):
            tastiness += u[flavors[i]][flavors[i+1]]
            cost += b
        
        # Update the maximum tastiness and cost if necessary
        if tastiness > max_tastiness or (tastiness == max_tastiness and cost < max_cost):
            max_tastiness, max_cost = tastiness, cost
    
    # Return the maximum possible tastiness per gold coin ratio
    if max_cost == 0:
        return 0
    else:
        return max_tastiness / max_cost

