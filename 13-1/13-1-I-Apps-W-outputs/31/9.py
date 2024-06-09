
def min_jumps_to_reach_home(n, d, s):
    # Initialize the minimum number of jumps to reach home
    min_jumps = 0
    # Initialize the current position of the frog
    current_position = 1
    # Loop through the string s
    for i in range(1, len(s)):
        # If the current position is not a lily pad, skip it
        if s[i] == "0":
            continue
        # If the current position is a lily pad and the distance to the next lily pad is less than or equal to the maximum jump distance, make the jump
        if current_position + d >= i:
            min_jumps += 1
            current_position = i
        # If the current position is a lily pad and the distance to the next lily pad is greater than the maximum jump distance, the frog can't reach home
        else:
            return -1
    # If the frog reaches the last lily pad, return the minimum number of jumps
    if current_position == n:
        return min_jumps
    # If the frog can't reach the last lily pad, return -1
    else:
        return -1

