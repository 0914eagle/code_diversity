
def f1(turn_sequence):
    # Convert the turn sequence to a list of directions
    directions = list(turn_sequence)

    # Initialize the number of possible unlock patterns to 0
    num_unlock_patterns = 0

    # Iterate over each pivot in the grid
    for pivot in range(1, 10):
        # If the direction at the current pivot is not a question mark, continue to the next pivot
        if directions[pivot - 1] != '?':
            continue

        # If the direction at the current pivot is a question mark, consider all possible directions
        for direction in ['L', 'R', 'S', 'A']:
            # Create a copy of the turn sequence with the current pivot replaced by the current direction
            modified_turn_sequence = directions[:]
            modified_turn_sequence[pivot - 1] = direction

            # If the modified turn sequence is consistent with the input, increment the number of possible unlock patterns
            if is_consistent_turn_sequence(modified_turn_sequence):
                num_unlock_patterns += 1

    return num_unlock_patterns

def f2(turn_sequence):
    # Convert the turn sequence to a list of directions
    directions = list(turn_sequence)

    # Initialize the number of possible unlock patterns to 0
    num_unlock_patterns = 0

    # Iterate over each pivot in the grid
    for pivot in range(1, 10):
        # If the direction at the current pivot is not a question mark, continue to the next pivot
        if directions[pivot - 1] != '?':
            continue

        # If the direction at the current pivot is a question mark, consider all possible directions
        for direction in ['L', 'R', 'S', 'A']:
            # Create a copy of the turn sequence with the current pivot replaced by the current direction
            modified_turn_sequence = directions[:]
            modified_turn_sequence[pivot - 1] = direction

            # If the modified turn sequence is consistent with the input, increment the number of possible unlock patterns
            if is_consistent_turn_sequence(modified_turn_sequence):
                num_unlock_patterns += 1

    return num_unlock_patterns

def is_consistent_turn_sequence(turn_sequence):
    # Convert the turn sequence to a list of directions
    directions = list(turn_sequence)

    # Initialize the current direction to 'S' (straight)
    current_direction = 'S'

    # Iterate over each pivot in the grid
    for pivot in range(1, 10):
        # Get the direction at the current pivot
        direction = directions[pivot - 1]

        # If the direction at the current pivot is a question mark, return False
        if direction == '?':
            return False

        # If the direction at the current pivot is not a question mark, check if it is consistent with the current direction
        if direction != current_direction:
            # If the direction at the current pivot is not consistent with the current direction, return False
            if direction == 'L' and current_direction == 'R':
                return False
            if direction == 'R' and current_direction == 'L':
                return False
            if direction == 'A' and current_direction != 'A':
                return False

        # Update the current direction to the direction at the current pivot
        current_direction = direction

    # If all directions are consistent, return True
    return True

if __name__ == '__main__':
    turn_sequence = input("Enter a turn sequence with some directional changes replaced by question marks: ")
    print(f"There are {f1(turn_sequence)} possible unlock patterns with the given turn sequence.")
    print(f"There are {f2(turn_sequence)} possible unlock patterns with the given turn sequence.")

