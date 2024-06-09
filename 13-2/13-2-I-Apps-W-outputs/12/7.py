
def solve(n, roads, q, length_changes):
    # Initialize a dictionary to store the current length of each road
    road_lengths = {}
    for road in roads:
        road_lengths[road[0]] = road[2]

    # Initialize a list to store the expected cost of building the network after each length change
    expected_costs = []

    # Loop through each length change
    for i in range(q):
        # Get the current length of the road that is going to be repaired
        current_length = road_lengths[length_changes[i][0]]
        # Get the new length of the road after the repair
        new_length = length_changes[i][1]
        # Calculate the difference in length
        length_diff = current_length - new_length

        # Loop through each road and update its length
        for road in roads:
            if road[0] == length_changes[i][0] or road[1] == length_changes[i][0]:
                road_lengths[road[0]] -= length_diff
                road_lengths[road[1]] -= length_diff

        # Calculate the expected cost of building the network after the length change
        expected_cost = 0
        for city in range(1, n + 1):
            for other_city in range(city + 1, n + 1):
                expected_cost += road_lengths[city] * road_lengths[other_city]
        expected_costs.append(expected_cost)

    return expected_costs

