
def min_jumps_to_reach_home(n, d, s):
    # Initialize the minimum number of jumps to reach home
    min_jumps = 0
    # Initialize the current position of the frog
    current_position = 1
    # Loop through the string s
    for i in range(1, len(s)):
        # If the current position is not a lily flower, skip it
        if s[i] == "0":
            continue
        # If the current position is a lily flower, check if we can jump to the next position
        if i - current_position <= d:
            # If we can jump, update the minimum number of jumps and the current position
            min_jumps += 1
            current_position = i
        # If we can't jump, return -1
        else:
            return -1
    # If we reach the end of the string and the current position is not the last position, return -1
    if current_position != n:
        return -1
    # Return the minimum number of jumps to reach home
    return min_jumps

