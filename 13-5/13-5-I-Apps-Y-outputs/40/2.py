
def solve(socks, capacity, k):
    # Sort the socks by color
    socks.sort()
    # Initialize the number of machines to 0
    machines = 0
    # Iterate over the socks
    for i in range(len(socks)):
        # Check if the current sock is further than k from the previous sock
        if i == 0 or abs(socks[i] - socks[i-1]) > k:
            # Increment the number of machines
            machines += 1
    # Return the number of machines
    return machines

