
def get_button_presses(current_state, desired_state):
    # Initialize the queue of button presses
    queue = []
    
    # Loop through the current state of the staircase room
    for i in range(len(current_state)):
        # Get the current floor and the floor it is connected to
        current_floor, connected_floor = current_state[i]
        
        # Get the desired floor and the floor it is connected to
        desired_floor, desired_connected_floor = desired_state[i]
        
        # If the current floor and the desired floor are not the same, add a red button press to the queue
        if current_floor != desired_floor:
            queue.append(("R", current_floor))
        
        # If the connected floors are not the same, add a green button press to the queue
        if connected_floor != desired_connected_floor:
            queue.append(("G", current_floor))
    
    # Return the queue of button presses
    return queue

def f1():
    # Read the input from stdin
    N, M = map(int, input().split())
    current_state = []
    desired_state = []
    for i in range(M):
        current_state.append(list(map(int, input().split())))
    for i in range(M):
        desired_state.append(list(map(int, input().split())))
    
    # Get the button presses
    queue = get_button_presses(current_state, desired_state)
    
    # Print the length of the queue
    print(len(queue))
    
    # Print the button presses
    for press in queue:
        print(press[0], press[1])

if __name__ == '__main__':
    f1()

