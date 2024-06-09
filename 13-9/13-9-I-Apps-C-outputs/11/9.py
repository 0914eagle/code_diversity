
def solve(wheels):
    # Initialize the minimum number of rotations to -1
    min_rotations = -1

    # Loop through each column of the first wheel
    for col in range(len(wheels[0])):
        # Initialize a set to store the unique letters in the column
        unique_letters = set()

        # Loop through each wheel and add the letter in the current column to the set
        for wheel in wheels:
            unique_letters.add(wheel[col])

        # If the set has only three unique letters, it is possible to rotate the wheels
        if len(unique_letters) == 3:
            # Increment the minimum number of rotations
            min_rotations += 1
        # If the set has more than three unique letters, it is not possible to rotate the wheels
        else:
            # Break out of the loop and return the minimum number of rotations
            break

    # Return the minimum number of rotations
    return min_rotations

