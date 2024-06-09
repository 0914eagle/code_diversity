
def f1(n, magnets):
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

def f2(n, magnets):
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

if __name__ == '__main__':
    n = int(input())
    magnets = [input() for _ in range(n)]
    print(f1(n, magnets))
    print(f2(n, magnets))

