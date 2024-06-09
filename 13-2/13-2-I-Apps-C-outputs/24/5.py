
def max_lights_on(n, s, a, b):
    # Initialize a list to store the on/off state of each light
    lights = [int(i) for i in s]
    # Initialize a list to store the maximum number of lights on at each second
    max_lights = [0] * (max(b) + 1)
    # Loop through each light
    for i in range(n):
        # Loop through each second when the light will toggle
        for j in range(b[i], len(max_lights), a[i]):
            # If the light is on, turn it off and decrease the number of lights on by 1
            if lights[i]:
                lights[i] = 0
                max_lights[j] -= 1
            # If the light is off, turn it on and increase the number of lights on by 1
            else:
                lights[i] = 1
                max_lights[j] += 1
    # Return the maximum number of lights on at any given second
    return max(max_lights)

