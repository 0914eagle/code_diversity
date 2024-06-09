
def is_prime(n: int) -> bool:
    
    # Check if n is greater than 1
    if n > 1:
        # Check for factors from 2 to sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    # If the number is less than or equal to 1, it is not prime
    return False

