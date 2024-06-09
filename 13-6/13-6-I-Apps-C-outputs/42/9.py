
def get_staircase_plan(current_state, desired_state, N):
    # Initialize the plan as a list of tuples (floor, button_type)
    plan = []
    
    # Iterate through the current state and compare it to the desired state
    for floor in range(N):
        # If the floor is not in the desired state, press the green button
        if floor not in desired_state:
            plan.append((floor, "G"))
        # If the floor is in the desired state, but not in the correct position, press the red button
        elif floor != desired_state[floor]:
            plan.append((floor, "R"))
    
    return plan

def get_button_presses(plan, N):
    # Initialize the button presses as an empty list
    button_presses = []
    
    # Iterate through the plan and add the corresponding button presses to the list
    for floor, button_type in plan:
        button_presses.append(f"{button_type} {floor}")
    
    return button_presses

def main():
    # Read the input data
    N, M = map(int, input().split())
    current_state = [int(x) for x in input().split()]
    desired_state = [int(x) for x in input().split()]
    
    # Get the staircase plan
    plan = get_staircase_plan(current_state, desired_state, N)
    
    # Get the button presses
    button_presses = get_button_presses(plan, N)
    
    # Print the number of button presses and the button presses
    print(len(button_presses))
    for button_press in button_presses:
        print(button_press)

if __name__ == '__main__':
    main()

