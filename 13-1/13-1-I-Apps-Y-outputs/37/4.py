
def solve(x):
    # Convert the apartment number to a string
    x_str = str(x)
    
    # Initialize a counter for the total number of digits pressed
    total_digits = 0
    
    # Iterate through each digit in the apartment number
    for digit in x_str:
        # Increment the counter for the total number of digits pressed
        total_digits += 1
        
        # If the digit is not the last digit in the apartment number, call the next apartment number
        if digit != x_str[-1]:
            # Call the next apartment number by appending the current digit to the end of the current apartment number
            next_apartment = x_str[:-1] + digit
            
            # Recursively call the solve function with the next apartment number
            total_digits += solve(next_apartment)
    
    # Return the total number of digits pressed
    return total_digits

