
def solve(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness, max_cost = 0, 0
    
    # Loop through all possible combinations of flavors
    for flavors in itertools.combinations(range(k), n):
        # Calculate the tastiness and cost of the current combination
        tastiness = sum(t[i] for i in flavors)
        cost = a * len(flavors) + b
        
        # Calculate the additional tastiness from complementary flavors
        for i in range(len(flavors) - 1):
            for j in range(i + 1, len(flavors)):
                tastiness += u[flavors[i]][flavors[j]]
        
        # Check if the current combination is the maximum
        if tastiness > max_tastiness or (tastiness == max_tastiness and cost < max_cost):
            max_tastiness, max_cost = tastiness, cost
    
    # Return the maximum tastiness per gold coin ratio
    if max_tastiness == 0:
        return 0
    else:
        return max_tastiness / max_cost

