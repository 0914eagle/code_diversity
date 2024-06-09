
def solve(n, magnets):
    # Initialize the cheapest price as the current price
    cheapest_price = int(''.join(magnets))
    
    # Iterate through all possible permutations of the magnets
    for perm in permutations(magnets):
        # Convert the permutation to an integer
        price = int(''.join(perm))
        
        # If the price is cheaper than the current cheapest price, update the cheapest price
        if price < cheapest_price:
            cheapest_price = price
    
    # Return the cheapest price
    return cheapest_price

