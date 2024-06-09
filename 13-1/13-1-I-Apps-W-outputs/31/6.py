
def min_jumps_to_reach_home(n, d, s):
    # Initialize the minimum number of jumps to reach home
    min_jumps = 0
    # Initialize the current position of the frog
    current_position = 1
    # Loop through each position from 1 to n
    for i in range(1, n):
        # If the current position is a lily flower
        if s[i] == "1":
            # Calculate the distance to the next lily flower
            distance = i - current_position
            # If the distance is less than or equal to the maximum jump distance
            if distance <= d:
                # Update the minimum number of jumps
                min_jumps += 1
                # Update the current position
                current_position = i
    # If the current position is not equal to the home position
    if current_position != n:
        # Return -1, indicating that the frog cannot reach home
        return -1
    # Return the minimum number of jumps
    return min_jumps

