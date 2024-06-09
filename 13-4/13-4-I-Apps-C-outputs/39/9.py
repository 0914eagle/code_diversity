
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    previous_light = "green"

    # Iterate through each traffic light
    for i in range(n - 1):
        light = traffic_lights[i]
        green_duration = light[1]
        red_duration = light[2]

        # If the current light is green, drive at constant speed
        if previous_light == "green":
            min_time += green_duration
            current_time += green_duration

        # If the current light is red, stop at the red light
        elif previous_light == "red":
            min_time += red_duration
            current_time = 0

        # Update the previous light
        previous_light = "green" if previous_light == "red" else "red"

    # Add the time to drive from the last traffic light to the end of the road
    min_time += n - current_time

    return min_time

