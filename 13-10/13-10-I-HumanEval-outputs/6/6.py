
def is_multiply_prime(a: int) -> bool:
    
    # Initialize a list to store the prime factors of a
    prime_factors = []
    
    # Loop through the numbers from 2 to the square root of a
    for i in range(2, int(a ** 0.5) + 1):
        # If the current number is divisible by a, it is not prime
        if a % i == 0:
            prime_factors.append(i)
    
    # If the length of the prime factors list is 3, return True
    if len(prime_factors) == 3:
        return True
    else:
        return False

