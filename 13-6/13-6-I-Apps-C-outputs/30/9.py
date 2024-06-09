
def get_max_simultaneously_on_lights(n, s, a, b):
    # Initialize a list to store the states of the lights
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a variable to store the maximum number of simultaneously on lights
    max_on_lights = 0
    
    # Iterate through each light
    for i in range(n):
        # Calculate the period of the light
        period = a[i]
        
        # Calculate the number of times the light will toggle
        num_toggles = (b[i] - 1) // period + 1
        
        # Iterate through each toggle of the light
        for j in range(num_toggles):
            # Calculate the time of the toggle
            toggle_time = b[i] + j * period
            
            # Toggle the light
            lights[i] ^= 1
            
            # Update the maximum number of simultaneously on lights
            max_on_lights = max(max_on_lights, sum(lights))
    
    return max_on_lights

