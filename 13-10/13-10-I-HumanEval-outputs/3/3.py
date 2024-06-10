
def change_base(x: int, base: int) -> str:
    
    # Convert the input number to a string in the current base
    x_str = str(x)
    # Initialize an empty string to store the converted number
    converted_str = ""
    # Loop through each digit of the input number
    for digit in x_str:
        # Convert the digit from the current base to the new base
        converted_digit = int(digit) * base
        # Add the converted digit to the converted number string
        converted_str += str(converted_digit)
    return converted_str

