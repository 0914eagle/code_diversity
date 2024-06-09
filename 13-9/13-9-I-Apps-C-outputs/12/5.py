
import math

def solve(n, traffic_lights):
    # Calculate the total duration of the traffic light cycle
    total_duration = 0
    for traffic_light in traffic_lights:
        total_duration += traffic_light[1] + traffic_light[2]
    
    # Calculate the probability that the car makes it through each traffic light
    probabilities = []
    for traffic_light in traffic_lights:
        probability = 1
        for other_traffic_light in traffic_lights:
            if other_traffic_light[0] < traffic_light[0]:
                probability *= other_traffic_light[1] / total_duration
            elif other_traffic_light[0] > traffic_light[0]:
                probability *= (other_traffic_light[1] + other_traffic_light[2]) / total_duration
        probabilities.append(probability)
    
    # Calculate the probability that the car makes it through all the traffic lights
    probability_all_lights = 1
    for probability in probabilities:
        probability_all_lights *= probability
    
    # Print the probability that each traffic light is the first red light hit
    for i in range(n):
        print(probabilities[i])
    
    # Print the probability that the car makes it through all the traffic lights
    print(probability_all_lights)

n = int(input())
traffic_lights = []
for i in range(n):
    x, r, g = map(int, input().split())
    traffic_lights.append((x, r, g))
solve(n, traffic_lights)

