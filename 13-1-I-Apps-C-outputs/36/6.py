
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
        # Get the index of the shop that sells the original version of the antique
        original_shop = antiques[i][0]
        
        # If the shop has not been visited yet, visit it and add the cost of the antique to the total cost
        if original_shop not in visited_shops:
            visited_shops.add(original_shop)
            total_cost += costs[i]
        
        # If we have visited all the required shops, return the total cost
        if len(visited_shops) == k:
            return total_cost
    
    # If we have not visited all the required shops, return -1
    return -1

