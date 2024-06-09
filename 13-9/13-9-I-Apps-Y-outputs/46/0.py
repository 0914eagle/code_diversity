
def solve(N, M):
    # Initialize a variable to store the number of ways to choose two balls
    # such that the sum is even
    num_ways = 0

    # Loop through all possible values of the first ball
    for i in range(1, N + M + 1):
        # If the first ball is even, the second ball must be odd to make the sum even
        if i % 2 == 0:
            # Increment the number of ways to choose two balls
            num_ways += M
        # If the first ball is odd, the second ball can be either even or odd to make the sum even
        else:
            num_ways += M + 1

    return num_ways

