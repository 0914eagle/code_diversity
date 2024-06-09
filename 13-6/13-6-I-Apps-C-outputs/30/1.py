
def solve(n, s, params):
    # Initialize the number of on lights to 0
    num_on_lights = 0
    # Initialize a list to store the on and off times of each light
    light_states = []

    # Iterate over the parameters of each light
    for i in range(n):
        # Extract the a and b parameters of the current light
        a, b = params[i]
        # If the current light is initially on
        if s[i] == "1":
            # Add the current light to the list of on lights
            light_states.append([b, b + a])
            # Increment the number of on lights
            num_on_lights += 1

    # Sort the list of on and off times of each light in ascending order
    light_states.sort()

    # Initialize the maximum number of on lights to 0
    max_on_lights = 0
    # Initialize a variable to store the current number of on lights
    current_on_lights = 0

    # Iterate over the sorted list of on and off times of each light
    for i in range(len(light_states)):
        # If the current light is on
        if light_states[i][0] <= i:
            # Increment the current number of on lights
            current_on_lights += 1
        # If the current light is off
        else:
            # Decrement the current number of on lights
            current_on_lights -= 1
        # Update the maximum number of on lights if necessary
        max_on_lights = max(max_on_lights, current_on_lights)

    # Return the maximum number of on lights
    return max_on_lights

