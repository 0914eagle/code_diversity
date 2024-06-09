
def get_points(x):
    # Find all possible factors of x
    factors = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            factors.append(i)
            if i * i != x:
                factors.append(x // i)
    
    # Sort factors in descending order
    factors.sort(reverse=True)
    
    # Calculate the number of factors
    num_factors = len(factors)
    
    # Return the number of factors minus 1, as the first factor is not counted
    return num_factors - 1

