
def is_achievable(s, x, y):
    # Initialize the current position and direction of the robot
    curr_pos = (0, 0)
    curr_dir = 0 # 0 = right, 1 = up, 2 = left, 3 = down

    # Iterate through the instruction sequence
    for instruction in s:
        if instruction == "F":
            # Move in the current direction by distance 1
            if curr_dir == 0:
                curr_pos = (curr_pos[0] + 1, curr_pos[1])
            elif curr_dir == 1:
                curr_pos = (curr_pos[0], curr_pos[1] + 1)
            elif curr_dir == 2:
                curr_pos = (curr_pos[0] - 1, curr_pos[1])
            else:
                curr_pos = (curr_pos[0], curr_pos[1] - 1)
        elif instruction == "T":
            # Turn 90 degrees
            curr_dir = (curr_dir + 1) % 4

    # Check if the final position is (x, y)
    return curr_pos == (x, y)

