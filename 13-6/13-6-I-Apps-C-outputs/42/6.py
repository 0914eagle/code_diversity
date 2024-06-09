
def f1(N, M, current_state, desired_state):
    # Initialize the sequence of button presses
    sequence = []

    # Loop through each floor
    for i in range(N):
        # Get the current and desired states of the staircase on floor i
        current_staircase = current_state[i]
        desired_staircase = desired_state[i]

        # If the current and desired states are the same, continue to the next floor
        if current_staircase == desired_staircase:
            continue

        # If the current state is not connected to any staircase, press the red button
        if current_staircase == -1:
            sequence.append(("R", i))
            continue

        # If the desired state is not connected to any staircase, press the green button
        if desired_staircase == -1:
            sequence.append(("G", i))
            continue

        # If the current state is connected to a staircase, but the desired state is not, press the green button
        if current_staircase != -1 and desired_staircase == -1:
            sequence.append(("G", i))
            continue

        # If the current state is not connected to the desired staircase, press the red button
        if current_staircase != desired_staircase:
            sequence.append(("R", i))
            continue

    # Return the sequence of button presses
    return sequence

def f2(N, M, current_state, desired_state):
    # Initialize the sequence of button presses
    sequence = []

    # Loop through each floor
    for i in range(N):
        # Get the current and desired states of the staircase on floor i
        current_staircase = current_state[i]
        desired_staircase = desired_state[i]

        # If the current and desired states are the same, continue to the next floor
        if current_staircase == desired_staircase:
            continue

        # If the current state is not connected to any staircase, press the red button
        if current_staircase == -1:
            sequence.append(("R", i))
            continue

        # If the desired state is not connected to any staircase, press the green button
        if desired_staircase == -1:
            sequence.append(("G", i))
            continue

        # If the current state is connected to a staircase, but the desired state is not, press the green button
        if current_staircase != -1 and desired_staircase == -1:
            sequence.append(("G", i))
            continue

        # If the current state is not connected to the desired staircase, press the red button
        if current_staircase != desired_staircase:
            sequence.append(("R", i))
            continue

    # Return the sequence of button presses
    return sequence

if __name__ == '__main__':
    # Read the input
    N, M = map(int, input().split())
    current_state = [-1] * N
    desired_state = [-1] * N
    for _ in range(M):
        i, j = map(int, input().split())
        current_state[i] = j
    for _ in range(M):
        i, j = map(int, input().split())
        desired_state[i] = j

    # Call the functions
    sequence1 = f1(N, M, current_state, desired_state)
    sequence2 = f2(N, M, current_state, desired_state)

    # Print the output
    print(len(sequence1))
    for button, floor in sequence1:
        print(button, floor)

