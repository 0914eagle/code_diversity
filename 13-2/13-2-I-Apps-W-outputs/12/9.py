
def solve(n, roads, q, length_changes):
    # Initialize a dictionary to store the current length of each road
    road_lengths = {}
    for road in roads:
        road_lengths[road[0]] = road[2]

    # Initialize a list to store the expected cost of building the network
    expected_costs = []

    # Loop through each length change
    for i in range(q):
        # Get the current length of the road that is being repaired
        current_length = road_lengths[length_changes[i][0]]

        # Calculate the new length of the road after the repair
        new_length = length_changes[i][1]

        # Calculate the difference in length between the current and new lengths
        length_diff = current_length - new_length

        # Loop through each road in the network
        for road in roads:
            # If the road is not the one that is being repaired
            if road[0] != length_changes[i][0]:
                # Calculate the new length of the road based on the length difference
                new_road_length = road_lengths[road[0]] - length_diff

                # Update the dictionary with the new length
                road_lengths[road[0]] = new_road_length

        # Calculate the expected cost of building the network after the repair
        expected_cost = 0
        for road in roads:
            expected_cost += road_lengths[road[0]]

        # Add the expected cost to the list of expected costs
        expected_costs.append(expected_cost)

    return expected_costs

