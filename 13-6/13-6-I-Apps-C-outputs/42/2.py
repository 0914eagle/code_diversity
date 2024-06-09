
def get_staircase_state(N, M):
    # Initialize the staircase state as a matrix with size N x N
    staircase_state = [[0] * N for _ in range(N)]
    
    # Iterate through the current state of the staircases
    for i in range(M):
        # Read the current state of the staircase
        curr_state = input().split()
        
        # Update the staircase state matrix
        staircase_state[int(curr_state[0])][int(curr_state[1])] = 1
    
    return staircase_state

def get_desired_state(N, M):
    # Initialize the desired state as a matrix with size N x N
    desired_state = [[0] * N for _ in range(N)]
    
    # Iterate through the desired state of the staircases
    for i in range(M):
        # Read the desired state of the staircase
        desired_state[int(input())] = 1
    
    return desired_state

def get_button_presses(staircase_state, desired_state):
    # Initialize the button presses as an empty list
    button_presses = []
    
    # Iterate through the rows of the staircase state matrix
    for i in range(len(staircase_state)):
        # Iterate through the columns of the staircase state matrix
        for j in range(len(staircase_state[i])):
            # If the current state of the staircase is different from the desired state
            if staircase_state[i][j] != desired_state[i][j]:
                # Add the button press to the list of button presses
                button_presses.append((i, j))
    
    return button_presses

def print_button_presses(button_presses):
    # Print the length of the list of button presses
    print(len(button_presses))
    
    # Iterate through the list of button presses
    for button_press in button_presses:
        # Print the button press
        print("R", button_press[0]) if button_press[1] == 1 else print("G", button_press[0])

if __name__ == '__main__':
    # Read the input
    N, M = map(int, input().split())
    
    # Get the current state of the staircases
    staircase_state = get_staircase_state(N, M)
    
    # Get the desired state of the staircases
    desired_state = get_desired_state(N, M)
    
    # Get the list of button presses
    button_presses = get_button_presses(staircase_state, desired_state)
    
    # Print the list of button presses
    print_button_presses(button_presses)

