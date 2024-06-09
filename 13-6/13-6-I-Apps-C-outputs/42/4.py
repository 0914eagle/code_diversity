
def get_button_presses(current_state, desired_state):
    # Initialize variables
    Q = 0
    button_presses = []

    # Loop through the current state and compare it to the desired state
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            # If the current state and desired state are different, add a button press to the list
            if current_state[i][j] != desired_state[i][j]:
                Q += 1
                button_presses.append((i, j))

    # Return the list of button presses
    return Q, button_presses

def f1(N, M, current_state, desired_state):
    # Get the button presses
    Q, button_presses = get_button_presses(current_state, desired_state)

    # Print the output
    print(Q)
    for i, j in button_presses:
        print("R" if current_state[i][j] == 0 else "G", i)

def f2(N, M, current_state, desired_state):
    # Get the button presses
    Q, button_presses = get_button_presses(current_state, desired_state)

    # Print the output
    print(Q)
    for i, j in button_presses:
        print("G" if current_state[i][j] == 0 else "R", i)

if __name__ == '__main__':
    N, M = map(int, input().split())
    current_state = []
    for i in range(N):
        current_state.append(list(map(int, input().split())))
    desired_state = []
    for i in range(N):
        desired_state.append(list(map(int, input().split())))
    f1(N, M, current_state, desired_state)
    f2(N, M, current_state, desired_state)

