
def solve(wheels):
    # Initialize the minimum number of rotations to -1
    min_rotations = -1

    # Loop through each wheel
    for wheel in wheels:
        # Check if the wheel has all unique letters
        if len(set(wheel)) != len(wheel):
            # If not, return -1
            return -1

    # If all wheels have unique letters, set the minimum number of rotations to 0
    min_rotations = 0

    # Loop through each wheel
    for wheel in wheels:
        # Find the index of the first occurrence of 'A' in the wheel
        index_A = wheel.index('A')

        # Find the index of the first occurrence of 'B' in the wheel
        index_B = wheel.index('B')

        # Find the index of the first occurrence of 'C' in the wheel
        index_C = wheel.index('C')

        # Calculate the minimum number of rotations required to align the letters
        min_rotations += min(abs(index_A - index_B), abs(index_A - index_C), abs(index_B - index_C))

    # Return the minimum number of rotations
    return min_rotations

