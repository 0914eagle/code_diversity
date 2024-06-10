
def is_multiply_prime(a: int) -> bool:
    
    # Initialize a list to store the prime numbers
    prime_numbers = []
    
    # Iterate from 2 to the square root of a
    for i in range(2, int(a ** 0.5) + 1):
        # Check if i is a prime number
        if a % i == 0:
            # If it is a prime number, add it to the list
            prime_numbers.append(i)
    
    # Check if the length of the list is 3
    return len(prime_numbers) == 3

