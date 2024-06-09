
def solve(current_state, desired_state):
    # Initialize the sequence of button presses
    sequence = []

    # Loop through the current state and compare it to the desired state
    for i in range(len(current_state)):
        # If the current state and desired state are not the same, add a button press to the sequence
        if current_state[i] != desired_state[i]:
            # Add a button press to the sequence
            sequence.append(i)

    # Return the sequence of button presses
    return sequence

