
def min_jumps(n, d, s):
    # Initialize the minimum number of jumps to reach home as -1
    min_jumps = -1
    # Initialize the current position as 1
    current_position = 1
    # Initialize the number of jumps as 0
    num_jumps = 0
    # Loop through each position from 1 to n
    for position in range(1, n + 1):
        # If the current position is the home, break the loop
        if position == n:
            break
        # If there is a lily flower in the current position, increment the current position by the maximum jump length
        if s[position - 1] == "1":
            current_position += d
        # Increment the number of jumps
        num_jumps += 1
    # If the current position is the home, set the minimum number of jumps to the number of jumps
    if current_position == n:
        min_jumps = num_jumps
    # Return the minimum number of jumps
    return min_jumps

