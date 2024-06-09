
def num_states(n):
    # Initialize the number of states to 1
    states = 1
    # Loop for each turn
    for i in range(n):
        # Double the number of states
        states *= 2
    # Return the number of states modulo 10^9 + 7
    return states % 1000000007

