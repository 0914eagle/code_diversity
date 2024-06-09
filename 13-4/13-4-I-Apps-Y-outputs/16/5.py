
def get_button_presses(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    button_presses = 0
    up_button_count = 0
    down_button_count = 0

    # Loop until the current floor is the goal floor or we reach the top or bottom of the building
    while current_floor != goal and (current_floor != 1 or current_floor != floors):
        # If the current floor is above the goal floor, press the down button
        if current_floor > goal:
            current_floor -= down
            down_button_count += 1
        # If the current floor is below the goal floor, press the up button
        elif current_floor < goal:
            current_floor += up
            up_button_count += 1

        # Increment the button press count
        button_presses += 1

    # If we reached the goal floor, return the number of button presses
    if current_floor == goal:
        return button_presses
    # If we reached the top or bottom of the building, return "use the stairs"
    else:
        return "use the stairs"

if __name__ == '__main__':
    floors = int(input())
    start = int(input())
    goal = int(input())
    up = int(input())
    down = int(input())
    print(get_button_presses(floors, start, goal, up, down))

