
def solve(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness = 0
    max_cost = 0
    
    # Loop through all possible combinations of scoops
    for i in range(1, n+1):
        for combination in itertools.combinations(range(k), i):
            # Calculate the tastiness and cost of the current combination
            tastiness = sum(t[i] for i in combination)
            cost = a * i + b
            
            # Calculate the tastiness per gold coin ratio
            ratio = tastiness / cost
            
            # Update the maximum tastiness and cost if the current combination is better
            if ratio > max_tastiness:
                max_tastiness = ratio
                max_cost = cost
    
    # Return the maximum tastiness per gold coin ratio
    return max_tastiness

