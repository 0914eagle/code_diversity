
def solve(current_state, desired_state):
    # Initialize variables
    N = len(current_state)
    M = len(desired_state)
    Q = 0
    red_button_presses = []
    green_button_presses = []

    # Loop through the current state and desired state
    for i in range(N):
        for j in range(N):
            # If the current state and desired state are different, add a button press
            if current_state[i][j] != desired_state[i][j]:
                Q += 1
                if current_state[i][j] == 1:
                    red_button_presses.append(i)
                else:
                    green_button_presses.append(i)

    # Add the button presses to the output
    output = []
    for i in range(Q):
        if i % 2 == 0:
            output.append("R " + str(red_button_presses[i // 2]))
        else:
            output.append("G " + str(green_button_presses[i // 2]))

    return output

