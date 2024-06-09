
import math

def get_light_probabilities(traffic_lights):
    # Calculate the probability that a car will make it through all the lights without stopping
    prob_all_lights = 1
    for light in traffic_lights:
        prob_light = get_light_probability(light)
        prob_all_lights *= prob_light
    
    # Calculate the probability that a car will hit a specific light
    prob_specific_light = 0
    for light in traffic_lights:
        prob_specific_light += get_light_probability(light) * light[0] / sum(map(lambda x: x[0], traffic_lights))
    
    return prob_all_lights, prob_specific_light

def get_light_probability(light):
    # Calculate the probability that a car will make it through a specific light without stopping
    x, r, g = light
    prob_red = r / (r + g)
    prob_green = g / (r + g)
    prob_all = prob_red + prob_green
    return prob_all

def main():
    n = int(input())
    traffic_lights = []
    for i in range(n):
        x, r, g = map(int, input().split())
        traffic_lights.append((x, r, g))
    
    prob_all_lights, prob_specific_light = get_light_probabilities(traffic_lights)
    print(f"{prob_all_lights:.6f}")
    print(f"{prob_specific_light:.6f}")

if __name__ == "__main__":
    main()

