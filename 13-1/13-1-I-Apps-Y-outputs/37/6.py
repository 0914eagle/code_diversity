
def solve(x):
    # Convert the apartment number to a string
    x_str = str(x)
    
    # Initialize a counter for the total number of digits pressed
    total_digits = 0
    
    # Iterate through each digit in the apartment number
    for digit in x_str:
        # Increment the counter for the total number of digits pressed
        total_digits += 1
        
        # If the digit is not the last digit in the apartment number,
        # call the next apartment number with the same digit
        if digit != x_str[-1]:
            # Call the next apartment number with the same digit
            next_apartment = int(digit + x_str[1:])
            
            # Add the number of digits in the next apartment number to the total
            total_digits += len(str(next_apartment))
    
    # Return the total number of digits pressed
    return total_digits

