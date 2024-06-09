
def get_button_presses(f, s, g, u, d):
    # Initialize variables
    pushes = 0
    current_floor = s

    # Loop until we reach the goal floor or exceed the number of floors
    while current_floor != g and current_floor <= f:
        # Calculate the distance to the goal floor
        distance = abs(g - current_floor)

        # Check if we can reach the goal floor with the UP button
        if distance <= u:
            # Press the UP button and update the current floor
            current_floor += distance
            pushes += 1

        # Check if we can reach the goal floor with the DOWN button
        elif distance <= d:
            # Press the DOWN button and update the current floor
            current_floor -= distance
            pushes += 1

        # We cannot reach the goal floor with either button
        else:
            return "use the stairs"

    # Return the number of button presses
    return pushes

