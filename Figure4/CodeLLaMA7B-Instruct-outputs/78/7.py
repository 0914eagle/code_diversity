

def hex_key(num):
    

    # Initialize a counter for the number of prime digits
    prime_count = 0

    # Iterate over the hexadecimal digits in the input string
    for digit in num:
        # Check if the current digit is a prime number
        if is_prime(digit):
            # If it is, increment the prime count
            prime_count += 1

    # Return the number of prime digits
    return prime_count

def is_prime(n):
    
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

[/PYTHON
