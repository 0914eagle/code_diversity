
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

        # Loop through each triple of cities
        for city1 in range(1, n + 1):
            for city2 in range(city1 + 1, n + 1):
                for city3 in range(city2 + 1, n + 1):
                    # Calculate the current cost of building the network between these cities
                    current_cost = road_lengths[city1] + road_lengths[city2] + road_lengths[city3]

                    # Calculate the new cost of building the network between these cities after the repair
                    new_cost = road_lengths[city1] + road_lengths[city2] + road_lengths[city3] - length_diff

                    # Add the difference in cost to the expected cost of building the network
                    expected_costs.append(new_cost - current_cost)

    # Return the list of expected costs
    return expected_costs

