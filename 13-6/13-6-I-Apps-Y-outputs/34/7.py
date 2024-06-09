
def elevator_buttons(floors, start, goal, up_button, down_button):
    # Initialize variables
    current_floor = start
    button_presses = 0

    # Loop until the goal floor is reached or it is impossible to reach the goal floor
    while current_floor != goal and current_floor >= 1 and current_floor <= floors:
        # Check if the goal floor is above the current floor
        if goal > current_floor:
            # Check if the up button can take you to the goal floor
            if goal - current_floor <= up_button:
                # Press the up button the necessary number of times
                button_presses += (goal - current_floor)
                current_floor = goal
            else:
                # Press the up button the maximum number of times
                button_presses += up_button
                current_floor += up_button
        else:
            # Check if the down button can take you to the goal floor
            if current_floor - goal <= down_button:
                # Press the down button the necessary number of times
                button_presses += (current_floor - goal)
                current_floor = goal
            else:
                # Press the down button the maximum number of times
                button_presses += down_button
                current_floor -= down_button

    # Check if the goal floor was reached
    if current_floor == goal:
        return button_presses
    else:
        return "use the stairs"

