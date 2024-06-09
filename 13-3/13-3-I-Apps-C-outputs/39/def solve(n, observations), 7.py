
def solve(n, observations):
    # Initialize a dictionary to store the parity of the costume for each child
    parity = {i: 0 for i in range(n)}

    # Iterate through the observations
    for i, (l, r, x) in enumerate(observations):
        # Get the indices of the children before and after the current child
        before = (i - l) % n
        after = (i + r + 1) % n

        # Update the parity of the costume for the current child
        parity[i] = x

        # Update the parity of the costume for the children before and after the current child
        parity[before] = (parity[before] + x) % 2
        parity[after] = (parity[after] + x) % 2

    # Initialize a variable to store the number of ways to assign costumes
    ways = 1

    # Iterate through the children
    for i in range(n):
        # If the parity of the costume for the current child is even, then the current child can wear either costume
        if parity[i] == 0:
            ways *= 2
        # If the parity of the costume for the current child is odd, then the current child must wear the other costume
        else:
            ways *= 1

    # Return the number of ways to assign costumes modulo 10^9 + 7
    return ways % 1000000007

