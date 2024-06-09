
def solve(n, observations):
    # Initialize the number of ways to assign costumes as 1
    num_ways = 1

    # Loop through each observation
    for observation in observations:
        # Get the number of children to the left and right of the current child
        l, r, x = observation

        # If the number of children is odd, then the current child must be wearing the orange pumpkin costume
        if l + r + 1 % 2 == 1:
            x = 1

        # Update the number of ways to assign costumes based on the parity of the number of children wearing the orange pumpkin costume
        num_ways *= 2 if x == 0 else 1

    # Return the number of ways to assign costumes modulo 10^9 + 7
    return num_ways % (10**9 + 7)

