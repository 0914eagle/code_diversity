
def solve(wheels):
    # Initialize the minimum number of rotations required to -1
    min_rotations = -1

    # Loop through each column of the first wheel
    for col in range(len(wheels[0])):
        # Initialize the set of letters in the current column to be empty
        letters = set()

        # Loop through each wheel and add the letter in the current column to the set
        for wheel in wheels:
            letters.add(wheel[col])

        # If the set of letters has more than 3 elements, return -1
        if len(letters) > 3:
            return -1

    # If we reach this point, all columns have at most 3 distinct letters, so return the minimum number of rotations required
    return min_rotations

