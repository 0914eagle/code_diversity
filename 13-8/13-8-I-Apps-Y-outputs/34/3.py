
def solve(x):
    # Find all possible factors of x
    factors = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            factors.append(i)
            if x // i != i:
                factors.append(x // i)
    
    # Sort the factors in descending order
    factors.sort(reverse=True)
    
    # Calculate the number of factors
    num_factors = len(factors)
    
    # Return the number of factors
    return num_factors

