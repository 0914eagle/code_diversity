
def get_staircase_plan(current_state, desired_state):
    # Initialize the plan as an empty list
    plan = []
    
    # Loop through the current state of the staircase room
    for floor in range(len(current_state)):
        # If the current state of the staircase room is different from the desired state, add a button press to the plan
        if current_state[floor] != desired_state[floor]:
            # Determine which button to press (red or green) based on the current state and desired state of the staircase room
            if current_state[floor] < desired_state[floor]:
                plan.append(("R", floor))
            else:
                plan.append(("G", floor))
    
    # Return the plan
    return plan

def get_button_presses(plan):
    # Initialize the button presses as an empty list
    button_presses = []
    
    # Loop through the plan and add the appropriate button presses to the list
    for action, floor in plan:
        if action == "R":
            button_presses.append(("R", floor))
        else:
            button_presses.append(("G", floor))
    
    # Return the button presses
    return button_presses

def main():
    # Read the input from stdin
    n, m = map(int, input().split())
    current_state = list(map(int, input().split()))
    desired_state = list(map(int, input().split()))
    
    # Get the staircase plan
    plan = get_staircase_plan(current_state, desired_state)
    
    # Get the button presses
    button_presses = get_button_presses(plan)
    
    # Print the length of the button presses
    print(len(button_presses))
    
    # Print the button presses
    for action, floor in button_presses:
        print(action, floor)

if __name__ == '__main__':
    main()

