
def get_unlock_patterns(turn_sequence):
    # Initialize a list to store the unlock patterns
    unlock_patterns = []
    
    # Iterate over the turn sequence
    for i in range(len(turn_sequence)):
        # If the current pivot is a question mark, add all four directional changes to the unlock pattern
        if turn_sequence[i] == '?':
            unlock_patterns.append('L' + unlock_patterns[-1][1:])
            unlock_patterns.append('R' + unlock_patterns[-1][1:])
            unlock_patterns.append('S' + unlock_patterns[-1][1:])
            unlock_patterns.append('A' + unlock_patterns[-1][1:])
        # Otherwise, add the current directional change to the unlock pattern
        else:
            unlock_patterns.append(turn_sequence[i] + unlock_patterns[-1][1:])
    
    # Return the number of unlock patterns
    return len(unlock_patterns)

