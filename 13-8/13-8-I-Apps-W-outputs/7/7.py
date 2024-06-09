
def max_number_from_cubes(cubes):
    # Initialize a list to store the digits of the numbers
    digits = []
    # Loop through each cube
    for cube in cubes:
        # Loop through each face of the cube
        for face in cube:
            # If the face is not zero, add it to the list of digits
            if face != 0:
                digits.append(face)
    # Sort the list of digits in descending order
    digits.sort(reverse=True)
    # Initialize a variable to store the maximum number
    max_num = 0
    # Loop through each digit in the list
    for digit in digits:
        # If the digit is 6 or 9, skip it
        if digit == 6 or digit == 9:
            continue
        # Add the digit to the maximum number
        max_num = max_num * 10 + digit
    # Return the maximum number
    return max_num

