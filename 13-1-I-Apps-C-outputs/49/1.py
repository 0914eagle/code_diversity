
def solve(current_state, desired_state):
    # Initialize the sequence of button presses
    sequence = []

    # Loop through the current state and compare it to the desired state
    for i in range(len(current_state)):
        # If the current state and desired state are the same, do nothing
        if current_state[i] == desired_state[i]:
            continue
        # If the current state and desired state are not the same, find the difference
        else:
            difference = current_state[i] - desired_state[i]
            # If the difference is 1, press the green button on floor i
            if difference == 1:
                sequence.append("G " + str(i))
            # If the difference is -1, press the red button on floor i
            elif difference == -1:
                sequence.append("R " + str(i))
            # If the difference is greater than 1, press the red button on floor i until the difference is 1
            elif difference > 1:
                for j in range(difference):
                    sequence.append("R " + str(i))
            # If the difference is less than -1, press the green button on floor i until the difference is -1
            elif difference < -1:
                for j in range(abs(difference)):
                    sequence.append("G " + str(i))

    # Return the sequence of button presses
    return sequence

