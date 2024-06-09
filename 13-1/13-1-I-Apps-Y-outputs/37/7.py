
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
        # add the number of digits in the remaining digits to the counter
        if digit != x_str[-1]:
            total_digits += len(x_str[x_str.index(digit) + 1:])
    
    # Return the total number of digits pressed
    return total_digits

