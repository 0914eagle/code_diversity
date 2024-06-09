
def is_achievable(s, x, y):
    # Initialize the current position and direction of the robot
    pos = [0, 0]
    dir = [1, 0]

    # Iterate through the instruction sequence
    for instruction in s:
        if instruction == "F":
            # Move in the current direction by distance 1
            pos[0] += dir[0]
            pos[1] += dir[1]
        elif instruction == "T":
            # Turn 90 degrees in the current direction
            dir = [-dir[1], dir[0]]

    # Check if the final position is (x, y)
    return pos == [x, y]

