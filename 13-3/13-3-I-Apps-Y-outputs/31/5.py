
import math

def get_min_distance(coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)

    # Initialize the minimum distance to be traveled
    min_distance = 0

    # Iterate through the sorted coordinates
    for i in range(len(sorted_coordinates)):
        # Calculate the distance between the current coordinate and the next coordinate
        distance = sorted_coordinates[i] - sorted_coordinates[i - 1] if i > 0 else sorted_coordinates[i]

        # Update the minimum distance if the current distance is less than the minimum distance
        if distance < min_distance or min_distance == 0:
            min_distance = distance

    return min_distance

n = int(input())
coordinates = list(map(int, input().split()))

print(get_min_distance(coordinates))

