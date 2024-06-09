
def get_min_time(n, traffic_lights):
    # Initialize variables
    current_time = 0
    total_time = 0
    distance = 0

    # Loop through each traffic light
    for i in range(n - 1):
        # Get the time, green duration, and red duration of the current light
        time, green, red = traffic_lights[i]

        # If the current time is before the start of the green duration, wait until the start of the green duration
        if current_time < time:
            current_time = time

        # If the current time is during the green duration, accelerate at a constant rate of 1 m/s^2 and update the distance traveled
        if time <= current_time < time + green:
            distance += (current_time - time) * 1
            current_time += 1

        # If the current time is during the red duration, stop on the spot and update the total time
        if time + green <= current_time < time + green + red:
            total_time += current_time - time
            current_time = time + green + red

    # Calculate the final distance traveled and add it to the total time
    distance += (current_time - time) * 1
    total_time += current_time

    # Return the minimum time required to reach the end of the road
    return total_time

