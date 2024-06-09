
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
    
    # Initialize a set to store the visited shops
    visited = set()
    
    # Initialize a variable to store the total cost
    total_cost = 0
    
    # Loop through each antique
    for a in antiques:
        # Get the original and knock-off versions of the antique
        original, knock_off = a[0], a[2]
        
        # If the original version of the antique is not in the dictionary, it means it has not been visited yet
        if original not in visited:
            # Add the cost of the original version of the antique to the total cost
            total_cost += costs[original]
            # Add the original version of the antique to the visited set
            visited.add(original)
        # If the knock-off version of the antique is not in the dictionary, it means it has not been visited yet
        elif knock_off not in visited:
            # Add the cost of the knock-off version of the antique to the total cost
            total_cost += costs[knock_off]
            # Add the knock-off version of the antique to the visited set
            visited.add(knock_off)
        # If both the original and knock-off versions of the antique have been visited, it means we cannot buy a version of this antique
        else:
            # Return -1 because it is not possible to collect all of the antiques while visiting no more than k stores
            return -1
    
    # If we have visited all k shops, return the total cost
    if len(visited) == k:
        return total_cost
    # If we have not visited all k shops, return -1
    else:
        return -1

