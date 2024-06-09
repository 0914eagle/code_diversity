
def get_button_presses(f, s, g, u, d):
    # Calculate the distance between the starting floor and the goal floor
    distance = abs(g - s)

    # Check if the distance is greater than the total number of floors
    if distance > f:
        return "use the stairs"

    # Initialize variables for the current floor and the number of button presses
    current_floor = s
    button_presses = 0

    # Loop until the current floor is the goal floor
    while current_floor != g:
        # Check if the current floor is less than the goal floor
        if current_floor < g:
            # Press the UP button to move up the elevator
            current_floor += u
            button_presses += 1
        else:
            # Press the DOWN button to move down the elevator
            current_floor -= d
            button_presses += 1

    # Return the number of button presses required to reach the goal floor
    return button_presses

