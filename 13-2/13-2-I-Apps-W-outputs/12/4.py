
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

        # Loop through each triple of cities and calculate the expected cost of building the network
        expected_cost = 0
        for city1 in range(1, n + 1):
            for city2 in range(city1 + 1, n + 1):
                for city3 in range(city2 + 1, n + 1):
                    if city1 != city2 and city2 != city3 and city1 != city3:
                        expected_cost += road_lengths[city1] + road_lengths[city2] + road_lengths[city3] - length_diff

        # Add the expected cost to the list of expected costs
        expected_costs.append(expected_cost / (n * (n - 1) * (n - 2) / 6))

    # Return the list of expected costs
    return expected_costs

