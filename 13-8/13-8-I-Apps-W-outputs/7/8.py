
def get_largest_number(cubes):
    # Initialize a set to store the unique digits
    unique_digits = set()
    
    # Loop through each cube
    for cube in cubes:
        # Loop through each face of the cube
        for face in cube:
            # Add the digit to the set if it's not already present
            if face not in unique_digits:
                unique_digits.add(face)
    
    # Initialize a variable to store the largest number
    largest_number = 0
    
    # Loop through the unique digits
    for digit in unique_digits:
        # Check if the digit is 6 or 9
        if digit in [6, 9]:
            # If it is, continue to the next digit
            continue
        # Add the digit to the largest number
        largest_number = largest_number * 10 + digit
    
    # Return the largest number
    return largest_number

