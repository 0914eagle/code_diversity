

def prime_length(string):
    
    # Check if the string length is a prime number
    if is_prime(len(string)):
        return True
    else:
        return False

def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
