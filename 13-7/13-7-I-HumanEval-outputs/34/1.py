
def is_multiply_prime(a: int) -> bool:
    
    # Initialize a list to store the prime factors of a
    prime_factors = []
    
    # Loop through the numbers from 2 to the square root of a
    for i in range(2, int(a ** 0.5) + 1):
        # If the current number is divisible by a, add it to the list of prime factors
        if a % i == 0:
            prime_factors.append(i)
    
    # Return True if there are exactly 3 prime factors, otherwise return False
    return len(prime_factors) == 3

