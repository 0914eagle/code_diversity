
def is_multiply_prime(a: int) -> bool:
    
    # Initialize a list to store the prime factors of a
    prime_factors = []
    
    # Iterate from 2 to the square root of a
    for i in range(2, int(a ** 0.5) + 1):
        # If i is a prime factor of a, add it to the list of prime factors
        if a % i == 0:
            prime_factors.append(i)
    
    # If the length of the list of prime factors is 3, return True
    if len(prime_factors) == 3:
        return True
    else:
        return False

