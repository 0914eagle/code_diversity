
def num_states(n):
    # Initialize the number of states to 1
    num_states = 1
    # Iterate over the number of moves
    for i in range(n):
        # Double the number of states
        num_states *= 2
        # Modulo 10^9 + 7 to avoid overflow
        num_states %= 1000000007
    # Return the number of states
    return num_states

