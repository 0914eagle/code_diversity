
def get_shortest_distance(distances, start, end):
    # Initialize the shortest distance as infinity
    shortest_distance = float('inf')
    # Loop through all the distances
    for i in range(len(distances)):
        # Calculate the distance from the start station to the current station
        distance = distances[start] + distances[end]
        # If the distance is less than the shortest distance, update the shortest distance
        if distance < shortest_distance:
            shortest_distance = distance
        # Move to the next station
        start = (start + 1) % len(distances)
        end = (end + 1) % len(distances)
    # Return the shortest distance
    return shortest_distance

def main():
    # Read the number of stations and the distances between them
    n = int(input())
    distances = [int(x) for x in input().split()]
    # Read the starting and ending stations
    start, end = [int(x) for x in input().split()]
    # Call the get_shortest_distance function to find the shortest distance between the starting and ending stations
    shortest_distance = get_shortest_distance(distances, start, end)
    # Print the shortest distance
    print(shortest_distance)

if __name__ == '__main__':
    main()

