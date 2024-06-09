
def solve(n, s, lights):
    # Initialize the maximum number of on lights
    max_on = 0
    # Initialize a dictionary to store the on and off times of each light
    light_times = {}

    # Iterate over the lights
    for i in range(n):
        # Get the parameters of the current light
        a, b = lights[i]
        # If the light is initially on
        if s[i] == "1":
            # Add the on time to the dictionary
            light_times[i] = [b, b + a]
        # If the light is initially off
        else:
            # Add the off time to the dictionary
            light_times[i] = [b + a, b + 2 * a]

    # Iterate over the times in the dictionary
    for time in sorted(light_times.values()):
        # If the time is on
        if time[0] % 2 == 0:
            # Increment the maximum number of on lights
            max_on += 1
        # If the time is off
        else:
            # Decrement the maximum number of on lights
            max_on -= 1

    return max_on

