
def get_button_presses(current_state, desired_state):
    # Initialize the queue of button presses
    queue = []
    
    # Loop through the current state and desired state
    for i in range(len(current_state)):
        # If the current state and desired state are not the same, add a button press to the queue
        if current_state[i] != desired_state[i]:
            # If the current state is 0 and the desired state is 1, add a red button press
            if current_state[i] == 0 and desired_state[i] == 1:
                queue.append("R " + str(i))
            # If the current state is 1 and the desired state is 0, add a green button press
            elif current_state[i] == 1 and desired_state[i] == 0:
                queue.append("G " + str(i))
    
    # Return the queue of button presses
    return queue

def main():
    # Read the input
    N, M = map(int, input().split())
    current_state = list(map(int, input().split()))
    desired_state = list(map(int, input().split()))
    
    # Get the button presses
    queue = get_button_presses(current_state, desired_state)
    
    # Print the length of the queue
    print(len(queue))
    
    # Print the button presses
    for press in queue:
        print(press)

if __name__ == '__main__':
    main()

