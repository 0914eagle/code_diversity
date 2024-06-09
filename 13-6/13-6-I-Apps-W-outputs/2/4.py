
def get_expected_length(n, roads):
    # Initialize a dictionary to store the length of each road
    lengths = {}
    for road in roads:
        lengths[road] = 1

    # Initialize a set to store the visited cities
    visited = set()
    visited.add(1)

    # Initialize the expected length to 0
    expected_length = 0

    # Loop through each city and calculate the expected length
    for city in range(1, n + 1):
        # If the city has not been visited, calculate the expected length
        if city not in visited:
            # Get the roads connected to the city
            connected_roads = [road for road in roads if city in road]

            # Calculate the expected length of each road
            expected_lengths = []
            for road in connected_roads:
                # If the road has not been visited, calculate the expected length
                if road not in visited:
                    # Get the length of the road
                    length = lengths[road]

                    # Calculate the probability of visiting the road
                    probability = 1 / len(connected_roads)

                    # Calculate the expected length of the road
                    expected_length = length * probability

                    # Add the expected length to the list
                    expected_lengths.append(expected_length)

            # Calculate the total expected length of the city
            expected_length += sum(expected_lengths)

        # Add the city to the visited set
        visited.add(city)

    # Return the expected length
    return expected_length

def main():
    # Read the input
    n = int(input())
    roads = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        roads.append((u, v))

    # Calculate the expected length
    expected_length = get_expected_length(n, roads)

    # Print the expected length
    print(expected_length)

if __name__ == '__main__':
    main()

