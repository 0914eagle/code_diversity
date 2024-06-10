
def get_good_observatories(observatories, roads):
    # Initialize a dictionary to store the elevation of each observatory
    observatory_elevations = {}
    for observatory in observatories:
        observatory_elevations[observatory] = observatories[observatory]

    # Initialize a dictionary to store the roads that can be reached from each observatory
    reachable_roads = {}
    for road in roads:
        if road[0] not in reachable_roads:
            reachable_roads[road[0]] = []
        reachable_roads[road[0]].append(road[1])

    # Initialize a set to store the good observatories
    good_observatories = set()

    # Iterate through each observatory and check if it is good
    for observatory in observatories:
        # If the observatory has no reachable roads, it is considered good
        if observatory not in reachable_roads:
            good_observatories.add(observatory)
            continue

        # If the observatory has reachable roads, check if its elevation is higher than that of all reachable observatories
        reachable_elevations = []
        for reachable_observatory in reachable_roads[observatory]:
            reachable_elevations.append(observatory_elevations[reachable_observatory])

        if observatories[observatory] > max(reachable_elevations):
            good_observatories.add(observatory)

    return len(good_observatories)

def main():
    # Read the input data
    num_observatories, num_roads = map(int, input().split())
    observatories = {}
    for i in range(num_observatories):
        observatories[i+1] = int(input())
    roads = []
    for i in range(num_roads):
        road = list(map(int, input().split()))
        roads.append(road)

    # Find the good observatories
    num_good_observatories = get_good_observatories(observatories, roads)

    # Print the result
    print(num_good_observatories)

if __name__ == '__main__':
    main()

