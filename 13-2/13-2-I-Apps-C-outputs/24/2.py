
def get_max_simultaneously_on_lights(n, s, a, b):
    # Initialize a list to store the states of the lights
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a variable to store the maximum number of simultaneously on lights
    max_on_lights = 0
    
    # Iterate through each light
    for i in range(n):
        # Calculate the time at which the light will toggle
        toggle_time = b[i] + a[i] * ((lights[i] + 1) // 2)
        
        # If the light is on, turn it off
        if lights[i] == 1:
            lights[i] = 0
        
        # If the light is off, turn it on
        else:
            lights[i] = 1
        
        # Update the maximum number of simultaneously on lights
        max_on_lights = max(max_on_lights, sum(lights))
    
    return max_on_lights

