
def get_number_of_lights_on(n, m, windows):
    # Initialize a counter for the number of lights on
    num_lights_on = 0

    # Iterate over each floor
    for floor in range(n):
        # Iterate over each window on the current floor
        for window in range(m):
            # Check if the current window has a light on
            if windows[floor][window] == "1":
                # Increment the counter for the number of lights on
                num_lights_on += 1

    # Return the number of lights on
    return num_lights_on

