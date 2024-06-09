
def max_lights_on(n, s, a, b):
    # Initialize a list to store the states of the lights
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a list to store the number of lights that are on at each moment
    moments = [0] * (max(a) + max(b))
    
    # Iterate over each light and its parameters
    for i in range(n):
        # Iterate over each moment when the light will toggle
        for j in range(b[i], max(a) + max(b), a[i]):
            # If the light is on, turn it off and decrease the number of lights that are on
            if lights[i]:
                lights[i] = 0
                moments[j] -= 1
            # If the light is off, turn it on and increase the number of lights that are on
            else:
                lights[i] = 1
                moments[j] += 1
    
    # Return the maximum number of lights that were on at the same time
    return max(moments)

