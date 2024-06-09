
def solve(socks, capacity, max_color_diff):
    # Sort the socks by color
    socks.sort()
    # Initialize the number of machines to 0
    num_machines = 0
    # Loop through the socks
    for i in range(len(socks)):
        # Check if the current sock is within the maximum color difference of the previous sock
        if i == 0 or abs(socks[i] - socks[i-1]) <= max_color_diff:
            # If it is, continue using the current machine
            continue
        else:
            # If it's not, start a new machine
            num_machines += 1
    # Return the number of machines needed
    return num_machines + 1

