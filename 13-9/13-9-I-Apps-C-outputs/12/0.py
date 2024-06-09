
import math

def get_light_probabilities(n):
    # Calculate the probability that an "ideal" car hits each light
    light_probabilities = []
    for i in range(n):
        light_probabilities.append(1 - math.exp(-1 * i / n))
    
    # Calculate the probability that an "ideal" car makes it all the way without stopping
    makes_it_probability = 1
    for i in range(n):
        makes_it_probability -= light_probabilities[i]
    
    return light_probabilities, makes_it_probability

n = int(input())
light_probabilities, makes_it_probability = get_light_probabilities(n)

for probability in light_probabilities:
    print(f"{probability:.6f}")
print(f"{makes_it_probability:.6f}")

