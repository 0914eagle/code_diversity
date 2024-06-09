
def solve(n, m, k, antiques):
    # Initialize a dictionary to store the costs of the antiques
    costs = {}
    
    # Loop through each antique
    for a in antiques:
        # Get the original and knock-off versions of the antique
        original, knock_off = a[0], a[2]
        
        # If the original version of the antique is not in the dictionary, add it with its cost
        if original not in costs:
            costs[original] = a[1]
        
        # If the knock-off version of the antique is not in the dictionary, add it with its cost
        if knock_off not in costs:
            costs[knock_off] = a[3]
    
    # Sort the dictionary by cost in ascending order
    sorted_costs = sorted(costs.items(), key=lambda x: x[1])
    
    # Initialize a variable to store the total cost
    total_cost = 0
    
    # Loop through the sorted dictionary and add the cost of each antique to the total cost
    for antique, cost in sorted_costs:
        total_cost += cost
        
        # If the total cost exceeds the maximum allowed cost, return -1
        if total_cost > k:
            return -1
    
    # Return the total cost
    return total_cost

