
def is_multiply_prime(a: int) -> bool:
    
    # Initialize a list to store the prime factors of a
    prime_factors = []
    
    # Loop through the numbers from 2 to the square root of a
    for i in range(2, int(a ** 0.5) + 1):
        # Check if i is a prime factor of a
        if a % i == 0:
            # Add the prime factor to the list
            prime_factors.append(i)
    
    # Check if the length of the list is 3
    return len(prime_factors) == 3

