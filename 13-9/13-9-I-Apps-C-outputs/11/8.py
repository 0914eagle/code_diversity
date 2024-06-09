
def solve(wheels):
    # Initialize the minimum number of rotations to -1
    min_rotations = -1

    # Loop through each wheel
    for wheel in wheels:
        # Check if the wheel has all distinct letters
        if len(set(wheel)) == 3:
            # If so, return 0
            return 0

    # Loop through each wheel
    for wheel in wheels:
        # Check if the wheel has two distinct letters
        if len(set(wheel)) == 2:
            # If so, set the minimum number of rotations to 1
            min_rotations = 1
            break

    # Loop through each wheel
    for wheel in wheels:
        # Check if the wheel has one distinct letter
        if len(set(wheel)) == 1:
            # If so, set the minimum number of rotations to 2
            min_rotations = 2
            break

    # Return the minimum number of rotations
    return min_rotations

