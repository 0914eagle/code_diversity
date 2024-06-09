
def get_maximum_positive_integer(A, K):
    # Find the greatest common divisor (GCD) of all elements in A
    gcd = A[0]
    for i in range(1, len(A)):
        gcd = gcd(gcd, A[i])
    
    # If K is 0, return the GCD
    if K == 0:
        return gcd
    
    # Initialize a list to store the factors of GCD
    factors = []
    
    # Iterate through the range of numbers from 1 to GCD and check if they are factors of GCD
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            factors.append(i)
    
    # Sort the factors in descending order
    factors.sort(reverse=True)
    
    # Initialize a variable to store the maximum possible positive integer that divides every element of A
    max_positive_integer = 1
    
    # Iterate through the factors and check if they are divisible by all elements of A
    for factor in factors:
        is_divisible = True
        for element in A:
            if element % factor != 0:
                is_divisible = False
                break
        if is_divisible:
            max_positive_integer = factor
            break
    
    # Return the maximum possible positive integer that divides every element of A
    return max_positive_integer

