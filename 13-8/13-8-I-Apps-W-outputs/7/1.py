
def get_largest_number(cubes):
    # Initialize a list to store the digits of the largest number
    largest_number = []
    
    # Iterate over the cubes
    for cube in cubes:
        # Iterate over the faces of the current cube
        for face in cube:
            # If the current face is not a zero, add it to the largest number
            if face != 0:
                largest_number.append(face)
    
    # Join the digits of the largest number into a string
    largest_number = "".join(str(digit) for digit in largest_number)
    
    # Return the largest number
    return int(largest_number)

