
def get_max_simultaneously_on_lights(n, s, a, b):
    # Initialize a list to store the states of the lights
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a variable to store the maximum number of simultaneously on lights
    max_on_lights = 0
    
    # Iterate through each light
    for i in range(n):
        # Calculate the period of the light
        period = a[i]
        
        # Calculate the phase of the light
        phase = b[i]
        
        # Iterate through each second
        for j in range(phase, phase + period * 2, period):
            # Toggle the state of the light
            lights[i] ^= 1
            
            # Update the maximum number of simultaneously on lights
            max_on_lights = max(max_on_lights, sum(lights))
    
    return max_on_lights

