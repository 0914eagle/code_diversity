
import math

def traffic_lights(n):
    # Initialize variables
    positions = []
    red_times = []
    green_times = []
    probabilities = []

    # Loop through each traffic light
    for i in range(n):
        # Read input for this traffic light
        x, r, g = map(int, input().split())
        positions.append(x)
        red_times.append(r)
        green_times.append(g)

        # Calculate probability of this light being the first red light
        probability = 0
        for j in range(n):
            if j == i:
                probability += (red_times[j] / (red_times[j] + green_times[j])) * (1 / n)
            else:
                probability += (red_times[j] / (red_times[j] + green_times[j])) * (1 / (n - 1))
        probabilities.append(probability)

    # Print output for each traffic light
    for i in range(n):
        print(f"{probabilities[i]:.6f}")

    # Calculate probability of car making it all the way without stopping
    probability = 1
    for i in range(n):
        probability *= 1 - (red_times[i] / (red_times[i] + green_times[i]))
    print(f"{probability:.6f}")

traffic_lights(int(input()))

