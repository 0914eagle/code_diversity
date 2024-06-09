
def repair_string(n, c):
    # Initialize an empty string
    s = ""
    
    # Iterate through the input sequence
    for i in range(n):
        # If the current position has a non-zero count
        if c[i] > 0:
            # Add the current letter to the string
            s += chr(i + ord('a'))
            # Decrement the count
            c[i] -= 1
    
    # Return the repaired string
    return s

