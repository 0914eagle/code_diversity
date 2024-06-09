
def solve(n, observations):
    # Initialize the number of ways to assign costumes as 1
    num_ways = 1

    # Iterate over each observation
    for observation in observations:
        # Get the number of children before, after, and at the center of view
        l, r, x = observation

        # If the number of children before and after is even, and the number of children at the center is odd, or vice versa
        if (l + r) % 2 == x:
            # The number of ways to assign costumes is 0
            return 0

        # If the number of children before and after is even, and the number of children at the center is even
        if l % 2 == r % 2 == x == 0:
            # The number of ways to assign costumes is doubled
            num_ways *= 2

        # If the number of children before and after is odd, and the number of children at the center is odd
        if l % 2 == r % 2 == x == 1:
            # The number of ways to assign costumes is doubled
            num_ways *= 2

    # Return the number of ways to assign costumes modulo 10^9 + 7
    return num_ways % (10**9 + 7)

