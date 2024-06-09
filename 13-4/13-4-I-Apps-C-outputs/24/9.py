
def solve(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness, max_cost = 0, 0
    
    # Loop through each possible number of scoops
    for num_scoops in range(1, n + 1):
        # Initialize the current tastiness and cost
        current_tastiness, current_cost = 0, 0
        
        # Loop through each possible combination of flavors
        for flavor_combination in itertools.combinations(range(k), num_scoops):
            # Calculate the tastiness of the current combination
            current_tastiness += sum(t[i] for i in flavor_combination)
            for i in range(len(flavor_combination)):
                for j in range(i + 1, len(flavor_combination)):
                    current_tastiness += u[flavor_combination[i]][flavor_combination[j]]
            
            # Calculate the cost of the current combination
            current_cost += a * num_scoops + b
            
            # Update the maximum tastiness and cost if necessary
            if current_tastiness > max_tastiness or (current_tastiness == max_tastiness and current_cost < max_cost):
                max_tastiness, max_cost = current_tastiness, current_cost
    
    # Return the maximum tastiness per gold coin ratio
    if max_tastiness == 0:
        return 0
    else:
        return max_tastiness / max_cost

