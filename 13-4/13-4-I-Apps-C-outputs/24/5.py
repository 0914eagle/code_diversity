
def solve(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness, max_cost = 0, 0
    
    # Loop through all possible combinations of flavors
    for i in range(1 << k):
        # Initialize the current tastiness and cost
        current_tastiness, current_cost = 0, 0
        
        # Loop through each flavor
        for j in range(k):
            # Check if the jth flavor is selected
            if i & (1 << j):
                # Add the tastiness of the current flavor to the total tastiness
                current_tastiness += t[j]
                # Add the cost of the current flavor to the total cost
                current_cost += a
        
        # Loop through all possible pairs of flavors
        for i in range(k):
            for j in range(i+1, k):
                # Check if the ith and jth flavors are selected
                if i & (1 << i) and j & (1 << j):
                    # Add the additional tastiness of the ith and jth flavors to the total tastiness
                    current_tastiness += u[i][j]
        
        # Check if the current combination is valid
        if current_cost <= n*b:
            # Update the maximum tastiness and cost if the current combination is better
            max_tastiness = max(max_tastiness, current_tastiness)
            max_cost = max(max_cost, current_cost)
    
    # Return the maximum tastiness per gold coin ratio
    return max_tastiness / max_cost if max_cost != 0 else 0

