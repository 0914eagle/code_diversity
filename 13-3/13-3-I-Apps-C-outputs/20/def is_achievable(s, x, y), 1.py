
def is_achievable(s, x, y):
    # Initialize the current position and direction of the robot
    pos = [0, 0]
    dir = 0 # 0 = right, 1 = up, 2 = left, 3 = down

    # Iterate through the instruction sequence
    for instruction in s:
        if instruction == "F":
            # Move in the current direction by distance 1
            if dir == 0:
                pos[0] += 1
            elif dir == 1:
                pos[1] += 1
            elif dir == 2:
                pos[0] -= 1
            else:
                pos[1] -= 1
        elif instruction == "T":
            # Turn 90 degrees
            dir = (dir + 1) % 4

    # Check if the final position is the desired one
    return pos[0] == x and pos[1] == y

