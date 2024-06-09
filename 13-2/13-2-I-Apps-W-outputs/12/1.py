
def solve(n, roads, q, length_changes):
    # Initialize a dictionary to store the current length of each road
    road_lengths = {}
    for road in roads:
        road_lengths[road[0]] = road[2]

    # Initialize a list to store the expected cost of building the network after each length change
    expected_costs = []

    # Loop through each length change
    for i in range(q):
        # Get the current length of the road that is being repaired
        current_length = road_lengths[length_changes[i][0]]

        # Calculate the expected cost of building the network after the length change
        expected_cost = 0
        for j in range(1, n + 1):
            for k in range(j + 1, n + 1):
                expected_cost += road_lengths[j] * road_lengths[k]
        expected_costs.append(expected_cost)

        # Update the length of the repaired road
        road_lengths[length_changes[i][0]] = length_changes[i][1]

    return expected_costs

