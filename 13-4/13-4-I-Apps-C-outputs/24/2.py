
def solve(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness, max_cost = 0, 0
    
    # Loop through all possible combinations of scoops
    for i in range(1, n+1):
        for j in range(1, n+1):
            for flavor1 in range(k):
                for flavor2 in range(k):
                    # Calculate the total tastiness and cost of the current combination
                    total_tastiness = t[flavor1] + t[flavor2] + u[flavor1][flavor2]
                    total_cost = a + b + i*a + j*a
                    
                    # Check if the current combination is the best so far
                    if total_tastiness > max_tastiness or (total_tastiness == max_tastiness and total_cost < max_cost):
                        max_tastiness, max_cost = total_tastiness, total_cost
    
    # Return the maximum tastiness per gold coin ratio
    if max_cost == 0:
        return 0
    else:
        return max_tastiness / max_cost

