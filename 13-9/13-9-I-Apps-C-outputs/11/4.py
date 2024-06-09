
def solve(wheels):
    # Initialize the number of rotations to 0
    rotations = 0

    # Loop through each wheel
    for wheel in wheels:
        # Check if the wheel has all three letters
        if "A" in wheel and "B" in wheel and "C" in wheel:
            # If the wheel has all three letters, continue to the next wheel
            continue
        else:
            # If the wheel does not have all three letters, rotate it to the right
            wheel = wheel[1:] + wheel[0]
            rotations += 1

    # Return the number of rotations required
    return rotations

