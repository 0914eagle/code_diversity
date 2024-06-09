
def get_button_presses(current_state, desired_state):
    # Initialize the button press sequence
    button_presses = []

    # Loop through the current state and compare it to the desired state
    for i in range(len(current_state)):
        # If the current state and desired state are not the same, add a button press to the sequence
        if current_state[i] != desired_state[i]:
            # Add a button press to the sequence
            button_presses.append(i)

    # Return the button press sequence
    return button_presses

def main():
    # Read the input
    N, M = map(int, input().split())
    current_state = [int(x) for x in input().split()]
    desired_state = [int(x) for x in input().split()]

    # Get the button press sequence
    button_presses = get_button_presses(current_state, desired_state)

    # Print the length of the button press sequence
    print(len(button_presses))

    # Print the button press sequence
    for i in button_presses:
        print("R " + str(i))

if __name__ == '__main__':
    main()

