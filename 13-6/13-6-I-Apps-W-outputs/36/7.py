
def get_min_price(n, prices, vitamins):
    # Initialize the minimum price to a large value
    min_price = float('inf')
    
    # Loop over all possible combinations of vitamins
    for vitamin_combination in itertools.combinations(vitamins, 3):
        # Initialize the current price to 0
        current_price = 0
        
        # Loop over all juices
        for i in range(n):
            # Check if the current juice contains the current vitamin combination
            if vitamins[i] == vitamin_combination:
                # Add the price of the current juice to the current price
                current_price += prices[i]
        
        # Check if the current price is less than the minimum price
        if current_price < min_price:
            # Update the minimum price
            min_price = current_price
    
    # Return the minimum price
    return min_price

