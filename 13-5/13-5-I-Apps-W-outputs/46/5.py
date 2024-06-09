
def f1(turn_sequence):
    # Replace '?' with 'L' or 'R' to make the turn sequence complete
    turn_sequence = turn_sequence.replace("?", "L")
    # Initialize a list to store the possible unlock patterns
    unlock_patterns = []
    # Loop through each pivot and its adjacent pivots
    for i in range(1, 9):
        # If the pivot is not the first or last pivot
        if i != 1 and i != 9:
            # Get the previous and next pivot
            prev_pivot = i - 1
            next_pivot = i + 1
            # If the turn sequence at the pivot is 'L'
            if turn_sequence[i - 2] == "L":
                # Add the pivot and its previous pivot to the unlock pattern
                unlock_patterns.append(str(prev_pivot) + str(i))
            # If the turn sequence at the pivot is 'R'
            elif turn_sequence[i - 2] == "R":
                # Add the pivot and its next pivot to the unlock pattern
                unlock_patterns.append(str(i) + str(next_pivot))
    # Return the number of possible unlock patterns
    return len(unlock_patterns)

def f2(turn_sequence):
    # Replace '?' with 'S' to make the turn sequence complete
    turn_sequence = turn_sequence.replace("?", "S")
    # Initialize a list to store the possible unlock patterns
    unlock_patterns = []
    # Loop through each pivot and its adjacent pivots
    for i in range(1, 9):
        # If the pivot is not the first or last pivot
        if i != 1 and i != 9:
            # Get the previous and next pivot
            prev_pivot = i - 1
            next_pivot = i + 1
            # If the turn sequence at the pivot is 'S'
            if turn_sequence[i - 2] == "S":
                # Add the pivot and its previous pivot to the unlock pattern
                unlock_patterns.append(str(prev_pivot) + str(i))
                # Add the pivot and its next pivot to the unlock pattern
                unlock_patterns.append(str(i) + str(next_pivot))
    # Return the number of possible unlock patterns
    return len(unlock_patterns)

if __name__ == '__main__':
    turn_sequence = input("Enter the turn sequence: ")
    print(f"The number of possible unlock patterns with a turn sequence matching the input is: {f1(turn_sequence)}")
    print(f"The number of possible unlock patterns with a turn sequence matching the input is: {f2(turn_sequence)}")

