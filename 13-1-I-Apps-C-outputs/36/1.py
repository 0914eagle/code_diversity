
def solve(n, m, k, antiques):
    # Initialize a dictionary to store the cost of each antique
    costs = {}
    
    # Loop through each antique
    for a in antiques:
        # Get the original and knock-off prices of the antique
        original_price, knockoff_price = a[1], a[3]
        
        # If the original price is less than the knock-off price, swap them
        if original_price > knockoff_price:
            original_price, knockoff_price = knockoff_price, original_price
        
        # Add the cost of the antique to the dictionary
        costs[a[0]] = original_price
    
    # Initialize a set to store the visited shops
    visited_shops = set()
    
    # Initialize a variable to store the total cost
    total_cost = 0
    
    # Loop through each antique
    for i in range(n):
        # Get the cost of the current antique
        cost = costs[i]
        
        # If the current antique has not been visited yet, visit it
        if i not in visited_shops:
            # Add the cost of the antique to the total cost
            total_cost += cost
            
            # Add the current antique to the set of visited shops
            visited_shops.add(i)
        
        # If the total number of visited shops is equal to k, return the total cost
        if len(visited_shops) == k:
            return total_cost
    
    # If it is not possible to visit all shops with a total cost of less than or equal to k, return -1
    return -1
