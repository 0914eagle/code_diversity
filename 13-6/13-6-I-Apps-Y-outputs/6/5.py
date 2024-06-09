
def get_min_distance(coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)
    # Initialize the minimum distance to 0
    min_distance = 0
    # Iterate over the sorted coordinates
    for i in range(len(sorted_coordinates)):
        # Calculate the distance between the current coordinate and the next coordinate
        distance = sorted_coordinates[i] - sorted_coordinates[i-1]
        # Update the minimum distance if the current distance is less than the minimum distance
        if distance < min_distance or min_distance == 0:
            min_distance = distance
    return min_distance

def main():
    # Read the number of houses and their coordinates from stdin
    num_houses = int(input())
    coordinates = list(map(int, input().split()))
    # Call the get_min_distance function and print the result
    print(get_min_distance(coordinates))

if __name__ == '__main__':
    main()

