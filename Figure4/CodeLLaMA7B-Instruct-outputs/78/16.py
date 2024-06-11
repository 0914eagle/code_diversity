

def hex_key(num):
    

    # Initialize the count to 0
    count = 0

    # Iterate over the characters in the input string
    for char in num:
        # Check if the character is a prime digit
        if char in ['2', '3', '5', '7', 'B', 'D']:
            # Increment the count if the character is a prime digit
            count += 1

    # Return the count
    return count


