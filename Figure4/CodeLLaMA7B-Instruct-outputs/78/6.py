

def hex_key(num):
    

    # Initialize a counter for the number of prime digits
    prime_digits = 0

    # Iterate over the digits of the hexadecimal number
    for digit in num:
        # Check if the digit is a prime number
        if is_prime(digit):
            # Increment the counter if the digit is prime
            prime_digits += 1

    return prime_digits

def is_prime(n):
    
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


