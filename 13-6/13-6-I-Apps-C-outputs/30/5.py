
def get_max_lights_on(n, s, a, b):
    # Initialize a list to store the state of each light
    lights = [1 if s[i] == "1" else 0 for i in range(n)]
    
    # Initialize a list to store the number of lights that are on at each second
    seconds = [0] * (max(b) + 1)
    
    # Loop through each light and its parameters
    for i in range(n):
        # Loop through each second when the light will toggle
        for j in range(b[i], max(b) + 1, a[i]):
            # If the light is on, turn it off
            if lights[i]:
                lights[i] = 0
                seconds[j] -= 1
            # If the light is off, turn it on
            else:
                lights[i] = 1
                seconds[j] += 1
    
    # Return the maximum number of lights that are on at the same time
    return max(seconds)

