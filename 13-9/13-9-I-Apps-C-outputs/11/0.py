
def solve(wheels):
    # Initialize the number of rotations to 0
    rotations = 0

    # Loop through each wheel
    for i in range(len(wheels)):
        # Get the current wheel
        wheel = wheels[i]

        # Check if the wheel has all distinct letters
        if len(set(wheel)) == len(wheel):
            # If the wheel has all distinct letters, continue to the next wheel
            continue

        # Get the index of the first occurrence of each letter in the wheel
        indices = [wheel.index(letter) for letter in "ABC"]

        # Check if the indices are in order
        if indices == [0, 1, 2]:
            # If the indices are in order, continue to the next wheel
            continue

        # Get the minimum number of rotations required to make the indices in order
        rotations += min(indices)

        # Rotate the wheel to the left by the minimum number of rotations
        wheels[i] = wheels[i][rotations:] + wheels[i][:rotations]

    # Check if all wheels have all distinct letters
    if len(set("".join(wheels))) == len("".join(wheels)):
        # If all wheels have all distinct letters, return the number of rotations
        return rotations
    else:
        # If not all wheels have all distinct letters, return -1
        return -1

