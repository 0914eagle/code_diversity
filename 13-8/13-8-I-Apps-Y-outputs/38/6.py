
def get_button_presses(f, s, g, u, d):
    # Calculate the difference between the starting floor and the goal floor
    diff = g - s

    # If the difference is zero, return 0 as there is no need to press any buttons
    if diff == 0:
        return 0

    # If the difference is negative, return "use the stairs" as the elevator cannot go downwards
    if diff < 0:
        return "use the stairs"

    # Initialize variables for the number of button presses and the current floor
    presses = 0
    current_floor = s

    # While the current floor is not the goal floor and the difference between the current floor and the goal floor is positive
    while current_floor != g and diff > 0:
        # If the difference is greater than or equal to the number of floors that the elevator can go up in one press
        if diff >= u:
            # Press the UP button the number of times necessary to reach the goal floor
            presses += diff // u
            current_floor = g
        # If the difference is less than the number of floors that the elevator can go up in one press
        else:
            # Press the UP button the number of times necessary to reach the maximum floor that the elevator can go up to
            presses += 1
            current_floor += u
            diff -= u

    # Return the number of button presses required to reach the goal floor
    return presses

