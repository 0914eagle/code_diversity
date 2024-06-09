
def get_largest_number(cubes):
    # Initialize a list to store the digits of the largest number
    largest_number = []

    # Iterate over the cubes
    for cube in cubes:
        # Iterate over the faces of the current cube
        for face in cube:
            # If the current face is not a 0, add it to the largest number
            if face != 0:
                largest_number.append(face)

    # Sort the largest number in descending order
    largest_number.sort(reverse=True)

    # Initialize a variable to store the largest number that can be made
    max_number = 0

    # Iterate over the digits of the largest number
    for digit in largest_number:
        # If the current digit is 6 or 9, skip it
        if digit == 6 or digit == 9:
            continue
        # Otherwise, add the current digit to the max number
        max_number = max_number * 10 + digit

    # Return the largest number that can be made
    return max_number

