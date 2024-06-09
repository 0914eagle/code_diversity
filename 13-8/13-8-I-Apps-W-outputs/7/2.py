
def get_largest_number(cubes):
    # Initialize a list to store the digits of the largest number
    largest_number = []

    # Iterate over the cubes and add the digits to the largest number
    for cube in cubes:
        for digit in cube:
            if digit not in largest_number and digit != 6 and digit != 9:
                largest_number.append(digit)

    # Sort the largest number in descending order
    largest_number.sort(reverse=True)

    # Convert the largest number to an integer and return it
    return int("".join(map(str, largest_number)))

