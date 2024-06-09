
def find_points(x):
    # Initialize a list to store the factors of x
    factors = []
    
    # Loop through all numbers from 1 to the square root of x
    for i in range(1, int(x**0.5) + 1):
        # If x is divisible by i, add it to the list of factors
        if x % i == 0:
            factors.append(i)
    
    # If x has a factor greater than its square root, add it to the list of factors
    if x > (int(x**0.5) + 1)**2:
        factors.append(int(x**0.5) + 1)
    
    # Return the number of factors
    return len(factors)

