
import math

def get_probability_of_red_light(x, r, g):
    # Calculate the probability of the car hitting the red light at time x
    probability = 0
    
    # Check if the car is within the range of the light
    if x >= 0 and x <= r:
        # Calculate the probability of the car hitting the light at time x
        probability = (x / r) ** 2
    
    return probability

def get_probability_of_making_it_through(x, r, g):
    # Calculate the probability of the car making it through all the lights
    probability = 1
    
    # Check if the car is within the range of the light
    if x >= 0 and x <= r:
        # Calculate the probability of the car making it through the light
        probability = 1 - (x / r) ** 2
    
    return probability

def main():
    n = int(input())
    lights = []
    
    for i in range(n):
        x, r, g = map(int, input().split())
        lights.append((x, r, g))
    
    # Calculate the probability of each light being the first red light hit
    for light in lights:
        print(get_probability_of_red_light(light[0], light[1], light[2]))
    
    # Calculate the probability of the car making it through all the lights
    probability = 1
    for light in lights:
        probability *= get_probability_of_making_it_through(light[0], light[1], light[2])
    print(probability)

if __name__ == '__main__':
    main()

