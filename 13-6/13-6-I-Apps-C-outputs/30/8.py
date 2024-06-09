
def solve(n, s, lights):
    # Initialize the maximum number of on lights
    max_on = 0
    # Initialize a dictionary to store the on/off status of each light
    light_status = {}
    # Iterate over the lights
    for i in range(n):
        # Get the current light and its parameters
        light, a, b = lights[i]
        # Check if the light is on or off
        if s[i] == "1":
            # If the light is on, mark it as on in the dictionary
            light_status[light] = True
        else:
            # If the light is off, mark it as off in the dictionary
            light_status[light] = False
        # Iterate over the periods of the light
        for j in range(a):
            # Get the current period
            period = b + j * a
            # Check if the light is on
            if light_status[light]:
                # If the light is on, turn it off
                light_status[light] = False
            else:
                # If the light is off, turn it on
                light_status[light] = True
            # Update the maximum number of on lights
            max_on = max(max_on, len(list(filter(lambda x: x[1], light_status.items()))))
    # Return the maximum number of on lights
    return max_on

