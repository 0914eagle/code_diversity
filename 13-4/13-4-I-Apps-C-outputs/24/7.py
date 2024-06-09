
def solve(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness = 0
    max_cost = 0
    
    # Loop through all possible combinations of flavors
    for i in range(1, k+1):
        for j in range(1, k+1):
            # Calculate the total tastiness and cost for this combination
            total_tastiness = t[i-1] + t[j-1] + u[i-1][j-1]
            total_cost = a + b
            
            # Check if this combination is better than the current maximum
            if total_tastiness > max_tastiness or (total_tastiness == max_tastiness and total_cost < max_cost):
                max_tastiness = total_tastiness
                max_cost = total_cost
    
    # Return the maximum tastiness and cost
    return max_tastiness, max_cost

