
def get_button_presses(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    button_presses = 0
    up_button_count = 0
    down_button_count = 0

    # Loop until the current floor is the goal floor or we have reached the top or bottom of the building
    while current_floor != goal and (current_floor > 1 or current_floor < floors):
        # Check if the current floor is higher than the goal floor
        if current_floor > goal:
            # Check if the down button can be pressed
            if down_button_count < current_floor - goal:
                # Press the down button
                current_floor -= down
                down_button_count += 1
            else:
                # Press the up button
                current_floor += up
                up_button_count += 1
        # Check if the current floor is lower than the goal floor
        elif current_floor < goal:
            # Check if the up button can be pressed
            if up_button_count < goal - current_floor:
                # Press the up button
                current_floor += up
                up_button_count += 1
            else:
                # Press the down button
                current_floor -= down
                down_button_count += 1

        # Increment the button press count
        button_presses += 1

    # Check if the current floor is the goal floor
    if current_floor == goal:
        return button_presses
    else:
        return "use the stairs"

if __name__ == '__main__':
    floors = int(input())
    start = int(input())
    goal = int(input())
    up = int(input())
    down = int(input())
    print(get_button_presses(floors, start, goal, up, down))

