
def f1(n, magnets):
    # Initialize the cheapest price as the current price
    cheapest_price = int(''.join(magnets))
    
    # Iterate through all possible permutations of the magnets
    for permutation in permutations(magnets):
        # Convert the permutation to an integer
        current_price = int(''.join(permutation))
        
        # If the current price is cheaper than the cheapest price, update the cheapest price
        if current_price < cheapest_price:
            cheapest_price = current_price
    
    # Return the cheapest price
    return cheapest_price

def f2(n, magnets):
    # Initialize the cheapest price as the current price
    cheapest_price = int(''.join(magnets))
    
    # Iterate through all possible permutations of the magnets
    for permutation in permutations(magnets):
        # Convert the permutation to an integer
        current_price = int(''.join(permutation))
        
        # If the current price is cheaper than the cheapest price, update the cheapest price
        if current_price < cheapest_price:
            cheapest_price = current_price
    
    # Return the cheapest price
    return cheapest_price

if __name__ == '__main__':
    n = int(input())
    magnets = input().split()
    print(f1(n, magnets))
    print(f2(n, magnets))

