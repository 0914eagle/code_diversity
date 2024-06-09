
def solve(n, m, k, antiques):
    # Initialize a dictionary to store the costs of the antiques
    costs = {}
    
    # Loop through each antique
    for a in antiques:
        # Get the original and knock-off prices of the antique
        original_price, knockoff_price = a[1], a[3]
        
        # If the original price is less than the knock-off price, swap them
        if original_price > knockoff_price:
            original_price, knockoff_price = knockoff_price, original_price
        
        # Add the costs of the antique to the dictionary
        costs[a[0]] = original_price
    
    # Initialize a set to store the visited shops
    visited_shops = set()
    
    # Initialize a variable to store the total cost
    total_cost = 0
    
    # Loop through each antique
    for i in range(n):
        # Get the cost of the current antique
        cost = costs[i]
        
        # If the current shop has not been visited yet, add the cost to the total cost and mark the shop as visited
        if costs[i] not in visited_shops:
            total_cost += cost
            visited_shops.add(costs[i])
    
    # If we have visited all the shops, return the total cost
    if len(visited_shops) == k:
        return total_cost
    
    # If we have not visited all the shops, return -1
    return -1

