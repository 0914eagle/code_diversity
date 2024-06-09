
def num_states(n):
    # Initialize the number of states to 1
    num_states = 1
    
    # Iterate over the number of moves
    for i in range(n):
        # Double the number of states
        num_states *= 2
    
    # Return the number of states modulo 10^9 + 7
    return num_states % 1000000007

