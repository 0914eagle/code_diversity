

def hex_key(num):
    

    # Initialize a counter for the number of prime digits
    prime_count = 0

    # Iterate over the characters in the input string
    for char in num:
        # Check if the current character is a prime digit
        if char in ['2', '3', '5', '7', 'B', 'D']:
            # If it is, increment the prime count
            prime_count += 1

    # Return the number of prime digits
    return prime_count


