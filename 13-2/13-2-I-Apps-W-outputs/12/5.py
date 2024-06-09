
def solve(n, roads, repairs):
    # Initialize a dictionary to store the length of each road
    road_lengths = {}
    for road in roads:
        road_lengths[road[0]] = road[2]

    # Initialize a list to store the expected cost of building the network
    expected_costs = []

    # Loop through each repair
    for repair in repairs:
        # Get the index of the road to be repaired and its new length
        road_index, new_length = repair[0], repair[1]

        # Update the length of the road in the dictionary
        road_lengths[road_index] = new_length

        # Calculate the expected cost of building the network
        expected_cost = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                expected_cost += road_lengths[i] * road_lengths[j]

        # Add the expected cost to the list of expected costs
        expected_costs.append(expected_cost)

    return expected_costs

