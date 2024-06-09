
def change_base(x: int, base: int) -> str:
    
    # Initialize an empty string to store the result
    result = ""
    
    # Loop until x is 0
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        # Add the remainder to the result string
        result = str(remainder) + result
        # Divide x by base
        x //= base
    
    # Return the result string
    return result

