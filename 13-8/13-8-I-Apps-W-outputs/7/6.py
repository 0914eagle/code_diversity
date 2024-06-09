
def max_number(cubes):
    # Initialize a set to store the unique numbers that can be formed
    unique_numbers = set()
    
    # Iterate over the cubes
    for cube in cubes:
        # Iterate over the digits of the cube
        for digit in cube:
            # If the digit is not already in the set, add it
            if digit not in unique_numbers:
                unique_numbers.add(digit)
    
    # Sort the unique numbers in descending order
    unique_numbers = sorted(unique_numbers, reverse=True)
    
    # Initialize a variable to store the maximum number that can be formed
    max_number = 0
    
    # Iterate over the unique numbers
    for number in unique_numbers:
        # If the number is already in the set, continue
        if number in unique_numbers:
            continue
        # If the number is not already in the set, add it and update the maximum number
        unique_numbers.add(number)
        max_number = number
    
    # Return the maximum number
    return max_number

