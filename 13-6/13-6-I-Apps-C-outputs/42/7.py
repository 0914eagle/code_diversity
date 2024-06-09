
def get_button_presses(current_state, desired_state):
    # Initialize the button press sequence
    button_presses = []

    # Loop through the current state and compare it to the desired state
    for i in range(len(current_state)):
        # If the current state and desired state are different, add a button press to the sequence
        if current_state[i] != desired_state[i]:
            # Determine which button to press based on the current state and desired state
            if current_state[i] > desired_state[i]:
                button_presses.append("R " + str(i))
            else:
                button_presses.append("G " + str(i))

    # Return the button press sequence
    return button_presses

def main():
    # Read the input
    N, M = map(int, input().split())
    current_state = list(map(int, input().split()))
    desired_state = list(map(int, input().split()))

    # Get the button press sequence
    button_presses = get_button_presses(current_state, desired_state)

    # Print the length of the button press sequence
    print(len(button_presses))

    # Print the button press sequence
    for button_press in button_presses:
        print(button_press)

if __name__ == '__main__':
    main()

