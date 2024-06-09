
def is_equal_to_sum_even(n: int) -> bool:
    
    # Initialize a list to store the factors
    factors = []
    
    # Iterate from 1 to the square root of n
    for i in range(1, int(n**0.5) + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # If it is, add it to the list of factors
            factors.append(i)
    
    # Check if any of the factors are even numbers
    for factor in factors:
        # If any factor is even, return True
        if factor % 2 == 0:
            return True
    
    # If no factors are even, return False
    return False

