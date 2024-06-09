
import math

def get_traffic_light_probabilities(traffic_lights):
    # Calculate the probability that the first red light is hit by an "ideal" car at each traffic light
    probabilities = []
    for traffic_light in traffic_lights:
        x, r, g = traffic_light
        probability = (g / (r + g)) ** 2
        probabilities.append(probability)
    
    # Calculate the probability that an "ideal" car makes it all the way without stopping
    total_probability = 1
    for i in range(len(traffic_lights)):
        total_probability *= 1 - probabilities[i]
    
    return probabilities, total_probability

def main():
    n = int(input())
    traffic_lights = []
    for i in range(n):
        x, r, g = map(int, input().split())
        traffic_lights.append((x, r, g))
    
    probabilities, total_probability = get_traffic_light_probabilities(traffic_lights)
    
    for probability in probabilities:
        print(f"{probability:.12f}")
    print(f"{total_probability:.12f}")

if __name__ == "__main__":
    main()

