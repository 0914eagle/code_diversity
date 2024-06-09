
def max_lights_on(n, s, a, b):
    # Initialize a list to store the states of the lights
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a list to store the maximum number of lights on at each moment
    max_lights = [0] * (max(b) + 1)
    
    # Loop through each light and its parameters
    for i in range(n):
        # Loop through each moment when the light will toggle
        for j in range(b[i], max(b) + 1, a[i]):
            # If the light is on, turn it off
            if lights[i] == 1:
                lights[i] = 0
            # If the light is off, turn it on
            else:
                lights[i] = 1
            # Update the maximum number of lights on at this moment
            max_lights[j] = max(max_lights[j], sum(lights))
    
    # Return the maximum number of lights on at any moment
    return max(max_lights)

