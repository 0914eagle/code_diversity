
def f1(turn_sequence):
    # Convert the turn sequence to a list of characters
    turn_sequence = list(turn_sequence)
    
    # Initialize a list to store the possible unlock patterns
    unlock_patterns = []
    
    # Iterate through the turn sequence
    for i in range(len(turn_sequence)):
        # If the current pivot is a question mark, add all four possible directions to the unlock pattern
        if turn_sequence[i] == '?':
            unlock_patterns.append('L')
            unlock_patterns.append('R')
            unlock_patterns.append('S')
            unlock_patterns.append('A')
        # Otherwise, add the current direction to the unlock pattern
        else:
            unlock_patterns.append(turn_sequence[i])
    
    # Return the number of possible unlock patterns
    return len(unlock_patterns)

def f2(turn_sequence):
    # Convert the turn sequence to a list of characters
    turn_sequence = list(turn_sequence)
    
    # Initialize a list to store the possible unlock patterns
    unlock_patterns = []
    
    # Iterate through the turn sequence
    for i in range(len(turn_sequence)):
        # If the current pivot is a question mark, add all four possible directions to the unlock pattern
        if turn_sequence[i] == '?':
            unlock_patterns.append('L')
            unlock_patterns.append('R')
            unlock_patterns.append('S')
            unlock_patterns.append('A')
        # Otherwise, add the current direction to the unlock pattern
        else:
            unlock_patterns.append(turn_sequence[i])
    
    # Return the number of possible unlock patterns
    return len(unlock_patterns)

if __name__ == '__main__':
    turn_sequence = input("Enter the turn sequence: ")
    print(f"The number of possible unlock patterns is {f1(turn_sequence)}")

