
def get_largest_number(cubes):
    # Initialize a list to store the digits of the number
    digits = []
    # Iterate over the cubes
    for cube in cubes:
        # Iterate over the faces of the cube
        for face in cube:
            # If the face is not a zero, add it to the digits list
            if face != 0:
                digits.append(face)
    # Sort the digits in descending order
    digits.sort(reverse=True)
    # Initialize a variable to store the largest number
    largest_number = 0
    # Initialize a variable to store the current number
    current_number = 0
    # Initialize a variable to store the power of 10
    power = 1
    # Iterate over the digits
    for digit in digits:
        # Add the current digit to the current number
        current_number += digit * power
        # Increment the power of 10
        power *= 10
        # If the current number is greater than the largest number, update the largest number
        if current_number > largest_number:
            largest_number = current_number
    # Return the largest number
    return largest_number

