
def get_good_observatories(observatories, roads):
    # Initialize a dictionary to keep track of the elevation of each observatory
    observatory_elevations = {}
    for observatory in observatories:
        observatory_elevations[observatory] = observatories[observatory]

    # Initialize a set to keep track of the good observatories
    good_observatories = set()

    # Loop through each road
    for road in roads:
        # Get the elevation of the starting observatory
        start_elevation = observatory_elevations[road[0]]

        # If the starting elevation is higher than the ending elevation, then the starting observatory is good
        if start_elevation > observatory_elevations[road[1]]:
            good_observatories.add(road[0])

    # Return the number of good observatories
    return len(good_observatories)

def main():
    # Read the number of observatories and roads from stdin
    num_observatories, num_roads = map(int, input().split())

    # Read the elevations of the observatories from stdin
    observatories = {}
    for i in range(num_observatories):
        observatories[i + 1] = int(input())

    # Read the roads from stdin
    roads = []
    for i in range(num_roads):
        road = list(map(int, input().split()))
        roads.append(road)

    # Call the get_good_observatories function and print the result
    print(get_good_observatories(observatories, roads))

if __name__ == '__main__':
    main()

