

def hex_key(num):
    

    # Initialize a counter for the number of prime digits
    prime_count = 0

    # Iterate over the characters in the input string
    for char in num:
        # Check if the character is a hexadecimal digit
        if char in "0123456789ABCDEF":
            # Convert the character to an integer
            digit = int(char, 16)
            # Check if the digit is prime
            if is_prime(digit):
                # Increment the count of prime digits
                prime_count += 1

    # Return the count of prime digits
    return prime_count

def
