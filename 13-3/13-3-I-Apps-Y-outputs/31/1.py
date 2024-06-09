
import math

def get_min_distance(coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)

    # Initialize the minimum distance to be traveled
    min_distance = 0

    # Loop through the sorted coordinates and calculate the distance between each pair of adjacent coordinates
    for i in range(len(sorted_coordinates) - 1):
        distance = sorted_coordinates[i + 1] - sorted_coordinates[i]
        min_distance += distance

    return min_distance

n = int(input())
coordinates = list(map(int, input().split()))

print(get_min_distance(coordinates))

