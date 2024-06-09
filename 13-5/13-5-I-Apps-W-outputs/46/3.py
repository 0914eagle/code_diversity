
def f1(turn_sequence):
    # Convert the turn sequence to a list of characters
    turn_sequence = list(turn_sequence)
    
    # Initialize the number of possible unlock patterns to 0
    num_patterns = 0
    
    # Loop through each pivot in the grid
    for i in range(1, 10):
        # If the pivot has not been visited yet, continue to the next pivot
        if i not in turn_sequence:
            continue
        
        # If the pivot has been visited, check if the directional change is consistent with the turn sequence
        if turn_sequence[i-1] == 'L' and i % 3 != 1:
            # If the pivot is not on the left edge of the grid and the directional change is 'L', continue to the next pivot
            continue
        elif turn_sequence[i-1] == 'R' and i % 3 != 0:
            # If the pivot is not on the right edge of the grid and the directional change is 'R', continue to the next pivot
            continue
        elif turn_sequence[i-1] == 'S' and (i % 3 == 1 or i % 3 == 0):
            # If the pivot is on the left or right edge of the grid and the directional change is 'S', continue to the next pivot
            continue
        elif turn_sequence[i-1] == 'A' and (i % 3 == 1 or i % 3 == 0):
            # If the pivot is on the left or right edge of the grid and the directional change is 'A', continue to the next pivot
            continue
        
        # If the pivot has been visited and the directional change is consistent with the turn sequence, increment the number of possible unlock patterns
        num_patterns += 1
    
    # Return the number of possible unlock patterns
    return num_patterns

def f2(turn_sequence):
    # Convert the turn sequence to a list of characters
    turn_sequence = list(turn_sequence)
    
    # Initialize the number of possible unlock patterns to 0
    num_patterns = 0
    
    # Loop through each pivot in the grid
    for i in range(1, 10):
        # If the pivot has not been visited yet, continue to the next pivot
        if i not in turn_sequence:
            continue
        
        # If the pivot has been visited, check if the directional change is consistent with the turn sequence
        if turn_sequence[i-1] == 'L' and i % 3 != 1:
            # If the pivot is not on the left edge of the grid and the directional change is 'L', continue to the next pivot
            continue
        elif turn_sequence[i-1] == 'R' and i % 3 != 0:
            # If the pivot is not on the right edge of the grid and the directional change is 'R', continue to the next pivot
            continue
        elif turn_sequence[i-1] == 'S' and (i % 3 == 1 or i % 3 == 0):
            # If the pivot is on the left or right edge of the grid and the directional change is 'S', continue to the next pivot
            continue
        elif turn_sequence[i-1] == 'A' and (i % 3 == 1 or i % 3 == 0):
            # If the pivot is on the left or right edge of the grid and the directional change is 'A', continue to the next pivot
            continue
        
        # If the pivot has been visited and the directional change is consistent with the turn sequence, increment the number of possible unlock patterns
        num_patterns += 1
    
    # Return the number of possible unlock patterns
    return num_patterns

if __name__ == '__main__':
    turn_sequence = input("Enter a turn sequence: ")
    print(f"There are {f1(turn_sequence)} possible unlock patterns that have a turn sequence matching the input.")
    print(f"There are {f2(turn_sequence)} possible unlock patterns that have a turn sequence matching the input.")

