
def solve(n, roads, repairs):
    # Initialize a dictionary to store the length of each road
    road_lengths = {}
    for road in roads:
        road_lengths[road[0]] = road[2]

    # Initialize a dictionary to store the expected cost of building the network
    expected_costs = {}
    for city1 in range(1, n + 1):
        for city2 in range(1, n + 1):
            if city1 < city2:
                expected_costs[(city1, city2)] = road_lengths[city1] + road_lengths[city2]
            else:
                expected_costs[(city1, city2)] = 0

    # Loop through the repairs and update the expected cost of building the network
    for repair in repairs:
        road, new_length = repair[0], repair[1]
        for city1 in range(1, n + 1):
            for city2 in range(1, n + 1):
                if city1 < city2:
                    expected_costs[(city1, city2)] += (new_length - road_lengths[road]) * (road_lengths[city1] + road_lengths[city2])
                else:
                    expected_costs[(city1, city2)] -= (new_length - road_lengths[road]) * (road_lengths[city1] + road_lengths[city2])
        road_lengths[road] = new_length

    return [expected_costs[(1, 2)] + expected_costs[(2, 3)] + expected_costs[(3, 1)] for _ in range(len(repairs))]

