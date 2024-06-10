
def calculate_minimum_distance(distances, p):
    # Sort the distances in ascending order
    sorted_distances = sorted(distances)
    
    # Initialize the minimum distance to the car directly in front
    minimum_distance = 0
    
    # Loop through the distances and calculate the minimum distance needed to maintain the given distance to the car in front
    for i in range(len(sorted_distances)):
        minimum_distance += sorted_distances[i] * (i + 1)
    
    # Return the minimum distance needed to maintain the given distance to the car in front
    return minimum_distance

def main():
    # Read the number of cars ahead and the deceleration constant from stdin
    n, p = map(int, input().split())
    
    # Read the current distances to each of the cars ahead from stdin
    distances = list(map(int, input().split()))
    
    # Calculate the minimum distance needed to maintain the given distance to the car in front
    minimum_distance = calculate_minimum_distance(distances, p)
    
    # Print the minimum distance needed to maintain the given distance to the car in front
    print(minimum_distance)

if __name__ == '__main__':
    main()

