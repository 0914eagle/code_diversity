
import math

def get_probabilities(traffic_lights):
    # Initialize variables
    n = len(traffic_lights)
    p_first_light = 0
    p_all_lights = 1

    # Loop through each traffic light
    for i in range(n):
        # Get the position, red duration, and green duration of the current light
        x, r, g = traffic_lights[i]

        # Calculate the probability that the car will hit this light
        p_hit_light = (x / 1000) * (1 / (r + g))

        # Calculate the probability that the car will make it through this light
        p_pass_light = 1 - p_hit_light

        # Update the probability that the car will make it through all the lights
        p_all_lights *= p_pass_light

        # If this is the first light, set the probability that it will be the first light hit
        if i == 0:
            p_first_light = p_hit_light

        # If this is not the first light, update the probability that it will be the first light hit
        else:
            p_first_light += p_hit_light * math.comb(n, i + 1)

    # Return the probabilities
    return p_first_light, p_all_lights

# Test the function with the sample input
traffic_lights = [(1, 2, 3), (6, 2, 3), (10, 2, 3), (16, 3, 4)]
p_first_light, p_all_lights = get_probabilities(traffic_lights)
print(f"Probability that the first light will be hit: {p_first_light:.6f}")
print(f"Probability that the car will make it through all the lights: {p_all_lights:.6f}")

# Test the function with a larger input
traffic_lights = [(1, 2, 3), (6, 2, 3), (10, 2, 3), (16, 3, 4), (21, 2, 3), (26, 2, 3), (30, 2, 3), (35, 2, 3), (40, 2, 3), (45, 2, 3), (50, 2, 3), (55, 2, 3), (60, 2, 3), (65, 2, 3), (70, 2, 3), (75, 2, 3), (80, 2, 3), (85, 2, 3), (90, 2, 3), (95, 2, 3), (100, 2, 3)]
p_first_light, p_all_lights = get_probabilities(traffic_lights)
print(f"Probability that the first light will be hit: {p_first_light:.6f}")
print(f"Probability that the car will make it through all the lights: {p_all_lights:.6f}")

