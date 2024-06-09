
def get_unlock_patterns(turn_sequence):
    # Initialize a list to store the unlock patterns
    unlock_patterns = []
    
    # Iterate through the turn sequence
    for i in range(len(turn_sequence)):
        # If the current pivot is a question mark, add all four directional changes to the unlock pattern
        if turn_sequence[i] == '?':
            unlock_patterns.append('L')
            unlock_patterns.append('R')
            unlock_patterns.append('S')
            unlock_patterns.append('A')
        # Otherwise, add the current directional change to the unlock pattern
        else:
            unlock_patterns.append(turn_sequence[i])
    
    # Return the list of unlock patterns
    return unlock_patterns

def count_consistent_unlock_patterns(turn_sequence):
    # Get the list of unlock patterns that match the turn sequence
    unlock_patterns = get_unlock_patterns(turn_sequence)
    
    # Initialize a counter to store the number of consistent unlock patterns
    count = 0
    
    # Iterate through the list of unlock patterns
    for unlock_pattern in unlock_patterns:
        # If the unlock pattern is consistent with the turn sequence, increment the counter
        if is_consistent_unlock_pattern(unlock_pattern, turn_sequence):
            count += 1
    
    # Return the number of consistent unlock patterns
    return count

def is_consistent_unlock_pattern(unlock_pattern, turn_sequence):
    # Initialize a flag to indicate whether the unlock pattern is consistent
    is_consistent = True
    
    # Iterate through the turn sequence
    for i in range(len(turn_sequence)):
        # If the current pivot is a question mark, continue to the next pivot
        if turn_sequence[i] == '?':
            continue
        # If the current pivot is not consistent with the unlock pattern, set the flag to False and break the loop
        if unlock_pattern[i] != turn_sequence[i]:
            is_consistent = False
            break
    
    # Return the flag
    return is_consistent

if __name__ == '__main__':
    turn_sequence = input("Enter a turn sequence with some directional changes replaced by question marks: ")
    print(f"There are {count_consistent_unlock_patterns(turn_sequence)} consistent unlock patterns with the turn sequence {turn_sequence}.")

