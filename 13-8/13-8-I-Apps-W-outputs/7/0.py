
def get_largest_number(n, cubes):
    # Initialize a set to store the unique digits
    unique_digits = set()
    
    # Iterate over the cubes
    for cube in cubes:
        # Add the digits to the set
        unique_digits |= set(cube)
    
    # Initialize a variable to store the largest number
    largest_number = 0
    
    # Iterate over the unique digits
    for digit in unique_digits:
        # Check if the digit is not 6 or 9
        if digit not in [6, 9]:
            # Initialize a variable to store the current number
            current_number = digit
            
            # Iterate over the cubes
            for cube in cubes:
                # Check if the current digit is in the cube
                if digit in cube:
                    # Add the digit to the current number
                    current_number = current_number * 10 + digit
            
            # Update the largest number
            largest_number = max(largest_number, current_number)
    
    # Return the largest number
    return largest_number

