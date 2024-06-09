
def solve(N):
    # Initialize the number of possible states to 1
    num_states = 1

    # Loop through each turn
    for turn in range(N):
        # Double the number of possible states
        num_states *= 2

    # Return the number of possible states modulo 10^9 + 7
    return num_states % 1000000007

