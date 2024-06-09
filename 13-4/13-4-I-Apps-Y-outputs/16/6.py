
def get_button_presses(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    button_presses = 0
    up_button_count = 0
    down_button_count = 0

    # Loop until the current floor is the goal floor or we reach the top or bottom of the building
    while current_floor != goal and (current_floor != 1 or current_floor != floors):
        # If the current floor is higher than the goal floor, press the down button
        if current_floor > goal:
            current_floor -= down
            down_button_count += 1
        # If the current floor is lower than the goal floor, press the up button
        else:
            current_floor += up
            up_button_count += 1
        # Increment the button press count
        button_presses += 1

    # If we reach the top or bottom of the building, return "use the stairs"
    if current_floor == 1 or current_floor == floors:
        return "use the stairs"
    # Otherwise, return the number of button presses
    else:
        return button_presses

def main():
    floors = int(input("Enter the number of floors: "))
    start = int(input("Enter the starting floor: "))
    goal = int(input("Enter the goal floor: "))
    up = int(input("Enter the number of floors the up button takes you: "))
    down = int(input("Enter the number of floors the down button takes you: "))
    print(get_button_presses(floors, start, goal, up, down))

if __name__ == '__main__':
    main()

