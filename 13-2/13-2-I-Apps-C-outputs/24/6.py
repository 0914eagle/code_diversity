
def get_max_simultaneously_on_lights(n, s, a, b):
    # Initialize a list to store the states of the lights
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a variable to store the maximum number of simultaneously on lights
    max_simultaneously_on = 0
    
    # Iterate through each light
    for i in range(n):
        # Calculate the time at which the light will toggle
        toggle_time = a[i] * (b[i] // a[i])
        
        # If the light is on, turn it off
        if lights[i] == 1:
            lights[i] = 0
            max_simultaneously_on -= 1
        
        # If the light is off, turn it on
        else:
            lights[i] = 1
            max_simultaneously_on += 1
        
        # Update the maximum number of simultaneously on lights
        max_simultaneously_on = max(max_simultaneously_on, sum(lights))
    
    return max_simultaneously_on

