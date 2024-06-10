
def get_desired_state(display):
    # Initialize the smallest possible state
    smallest_state = "9" * len(display)

    # Iterate through all possible states
    for i in range(10 ** len(display)):
        # Convert the state to a string
        state_str = str(i)

        # Pad the state with leading zeros
        state_str = state_str.zfill(len(display))

        # Get the next state by applying the buttons
        next_state = get_next_state(state_str)

        # Check if the current state is smaller than the smallest state
        if next_state < smallest_state:
            smallest_state = next_state

    return smallest_state

def get_next_state(state):
    # Add 1 to all digits
    next_state = str(int(state) + 1)

    # Shift all digits one position to the right
    next_state = next_state[1:] + next_state[0]

    return next_state

if __name__ == '__main__':
    display = input()
    print(get_desired_state(display))

