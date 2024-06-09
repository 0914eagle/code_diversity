
def get_largest_number(cubes):
    # Initialize a list to store the digits of the largest number
    largest_number = []
    # Loop through each cube
    for cube in cubes:
        # Loop through each face of the cube
        for face in cube:
            # If the face is not a 0, add it to the largest number
            if face != 0:
                largest_number.append(face)
    # Join the largest number into a string
    largest_number = "".join(str(digit) for digit in largest_number)
    # Return the largest number
    return largest_number

