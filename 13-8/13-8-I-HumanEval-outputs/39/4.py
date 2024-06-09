
def change_base(x: int, base: int) -> str:
    
    # Convert the input number to a string in the current base
    x_str = str(x)
    # Initialize an empty string to store the result
    result = ""
    # Loop through the digits of the input number
    for digit in x_str:
        # Convert the digit to an integer
        digit_int = int(digit)
        # Convert the digit to a string in the new base
        digit_str = str(digit_int)
        # Add the digit string to the result
        result += digit_str
    return result

