
def num_states(n):
    # Initialize a list to store the number of states for each turn
    states = [1, 1]
    
    # Iterate from the second turn to the last turn
    for i in range(2, n+1):
        # Calculate the number of states for the current turn
        states.append(states[i-1] * 2)
    
    # Return the total number of states modulo 10^9 + 7
    return states[-1] % 1000000007

