
def solve(n, s, parameters):
    # Initialize the number of on lights to 0
    num_on_lights = 0
    # Initialize a list to store the on and off times of each light
    light_times = []

    # Iterate over the parameters of each light
    for i in range(n):
        # Get the on and off times of the current light
        on_time, off_time = parameters[i]
        # If the light is initially on, add its on time to the list
        if s[i] == "1":
            light_times.append(on_time)
        # If the light is initially off, add its off time to the list
        else:
            light_times.append(off_time)

    # Sort the list of on and off times in ascending order
    light_times.sort()

    # Iterate over the sorted list of on and off times
    for i in range(len(light_times)):
        # If the current time is an on time, increase the number of on lights
        if light_times[i] % 2 == 1:
            num_on_lights += 1
        # If the current time is an off time, decrease the number of on lights
        else:
            num_on_lights -= 1

    # Return the maximum number of on lights
    return num_on_lights

