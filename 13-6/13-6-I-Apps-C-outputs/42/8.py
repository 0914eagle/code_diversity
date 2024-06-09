
def get_button_presses(current_state, desired_state):
    # Initialize the button press sequence
    button_presses = []

    # Loop through each floor
    for floor in range(len(current_state)):
        # Get the current and desired states of the floor
        current_floor_state = current_state[floor]
        desired_floor_state = desired_state[floor]

        # If the current and desired states are different, add a button press to the sequence
        if current_floor_state != desired_floor_state:
            # Determine which button to press (red or green)
            if current_floor_state > desired_floor_state:
                button_press = "R " + str(floor)
            else:
                button_press = "G " + str(floor)

            # Add the button press to the sequence
            button_presses.append(button_press)

    # Return the button press sequence
    return button_presses

def main():
    # Read the input
    N, M = map(int, input().split())
    current_state = []
    desired_state = []
    for _ in range(M):
        i, j = map(int, input().split())
        current_state.append(i)
        desired_state.append(j)

    # Get the button press sequence
    button_presses = get_button_presses(current_state, desired_state)

    # Print the output
    print(len(button_presses))
    for button_press in button_presses:
        print(button_press)

if __name__ == '__main__':
    main()

