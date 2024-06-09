
def max_lights_on(n, s, a, b):
    # Initialize a list to store the states of the lights
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a list to store the maximum number of lights on at any time
    max_lights = [0]
    
    # Iterate over the lights and their parameters
    for i in range(n):
        # Calculate the time at which the light will toggle
        toggle_time = b[i] + a[i] * (1 + int(not lights[i]))
        
        # If the toggle time is greater than the current time, increase the number of lights on
        if toggle_time > max_lights[-1]:
            max_lights.append(max_lights[-1] + 1)
        # Otherwise, decrease the number of lights on
        else:
            max_lights.append(max_lights[-1] - 1)
        
        # Toggle the state of the light
        lights[i] = 1 - lights[i]
    
    # Return the maximum number of lights on at any time
    return max(max_lights)

