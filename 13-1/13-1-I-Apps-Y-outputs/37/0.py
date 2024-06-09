
def solve(x):
    # Convert the apartment number to a string
    x_str = str(x)
    
    # Initialize a counter for the total number of digits pressed
    total_digits = 0
    
    # Iterate through each digit in the apartment number
    for digit in x_str:
        # Convert the digit to an integer
        digit = int(digit)
        
        # Calculate the number of digits pressed for this digit
        num_digits = digit * (digit + 1) // 2
        
        # Add the number of digits pressed for this digit to the total
        total_digits += num_digits
    
    # Return the total number of digits pressed
    return total_digits

