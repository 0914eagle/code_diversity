
def solve(n, roads, repairs):
    # Initialize a dictionary to store the length of each road
    road_lengths = {}
    for road in roads:
        a, b, length = road
        road_lengths[(a, b)] = length
        road_lengths[(b, a)] = length
    
    # Initialize a dictionary to store the expected cost of building the network
    expected_cost = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                expected_cost[(i, j, k)] = road_lengths[(i, j)] + road_lengths[(j, k)] + road_lengths[(k, i)]
    
    # Apply the repairs
    for repair in repairs:
        road, new_length = repair
        old_length = road_lengths[road]
        difference = new_length - old_length
        for key in expected_cost:
            if key[0] == road[0] or key[1] == road[1]:
                expected_cost[key] += difference
    
    # Return the expected cost of building the network
    return expected_cost

