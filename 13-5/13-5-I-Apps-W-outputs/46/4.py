
def get_unlock_patterns(turn_sequence):
    # Initialize a list to store the unlock patterns
    unlock_patterns = []
    
    # Iterate through each pivot in the turn sequence
    for i in range(len(turn_sequence)):
        # If the current pivot is a question mark, add all four possible directions to the unlock pattern
        if turn_sequence[i] == '?':
            unlock_patterns.append(turn_sequence[:i] + 'L' + turn_sequence[i+1:])
            unlock_patterns.append(turn_sequence[:i] + 'R' + turn_sequence[i+1:])
            unlock_patterns.append(turn_sequence[:i] + 'S' + turn_sequence[i+1:])
            unlock_patterns.append(turn_sequence[:i] + 'A' + turn_sequence[i+1:])
        # If the current pivot is not a question mark, add the current direction to the unlock pattern
        else:
            unlock_patterns.append(turn_sequence[:i] + turn_sequence[i] + turn_sequence[i+1:])
    
    # Return the number of unlock patterns
    return len(unlock_patterns)

def main():
    # Take input from the user
    turn_sequence = input("Enter a turn sequence with question marks for any directional changes: ")
    
    # Call the get_unlock_patterns function and print the result
    print(get_unlock_patterns(turn_sequence))

if __name__ == '__main__':
    main()

