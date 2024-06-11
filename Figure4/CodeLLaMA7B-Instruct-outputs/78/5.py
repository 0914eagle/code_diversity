

def hex_key(num):
    

    # Initialize a counter for the number of prime digits
    prime_digits = 0

    # Iterate over the characters in the input string
    for char in num:
        # Check if the current character is a hexadecimal digit
        if char in "0123456789ABCDEF":
            # Convert the character to an integer
            digit = int(char, 16)
            # Check if the digit is prime
            if is_prime(digit):
                # Increment the counter if the digit is prime
                prime_digits += 1

    # Return the number of prime digits
    return prime_digits

def is_prime(n):
    
    if n < 2:
        return False
