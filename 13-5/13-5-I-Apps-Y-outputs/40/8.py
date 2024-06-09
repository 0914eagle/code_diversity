
def solve(socks, capacity, k):
    # Sort the socks by color
    socks.sort()
    # Initialize the number of machines to 0
    machines = 0
    # Iterate over the socks
    for i in range(len(socks)):
        # Check if the current sock is within the range of the previous sock
        if i > 0 and abs(socks[i] - socks[i-1]) <= k:
            # If it is, continue using the same machine
            continue
        # If it's not, start a new machine
        machines += 1
    # Return the number of machines needed
    return machines

