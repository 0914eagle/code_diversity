
import math

def traffic_lights(n, lights):
    # Initialize variables
    prob_first_light = 0
    prob_all_the_way = 1

    # Loop through each light
    for i in range(n):
        # Get the current light's position and durations
        x, r, g = lights[i]

        # Calculate the probability of hitting this light
        prob_hit = (r / (r + g)) * (1 / (2019 - x))

        # Update the probability of hitting the first light
        prob_first_light += prob_hit

        # Update the probability of making it all the way
        prob_all_the_way *= (1 - prob_hit)

    # Return the probabilities
    return prob_first_light, prob_all_the_way

# Main function
n = int(input())
lights = []
for i in range(n):
    x, r, g = map(int, input().split())
    lights.append((x, r, g))

prob_first_light, prob_all_the_way = traffic_lights(n, lights)
print(prob_first_light)
print(prob_all_the_way)

