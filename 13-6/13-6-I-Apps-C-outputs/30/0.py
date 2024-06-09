
def max_lights_on(n, s, *lights):
    # Initialize a list to store the on/off state of each light
    light_states = [int(s[i]) for i in range(n)]
    
    # Initialize a list to store the maximum number of lights on at any moment
    max_lights_on_list = [0]
    
    # Iterate through each light and its parameters
    for i, (a, b) in enumerate(lights):
        # Determine the on/off state of the light at each moment
        light_states = [1 - light_states[i] if j % (a * 2) == b else light_states[i] for j in range(max(light_states))]
        
        # Update the maximum number of lights on at any moment
        max_lights_on_list.append(max(max_lights_on_list[-1], sum(light_states)))
    
    # Return the maximum number of lights on at any moment
    return max_lights_on_list[-1]

