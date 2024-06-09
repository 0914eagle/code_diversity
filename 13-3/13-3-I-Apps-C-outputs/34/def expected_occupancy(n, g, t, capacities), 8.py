
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of each group size
    probabilities = [i/g for i in range(1, g+1)]

    # Calculate the expected number of people in the restaurant at the end of each hour
    expected_occupancy = [0] * (t+1)
    for i in range(t):
        for j in range(n):
            expected_occupancy[i+1] += probabilities[i%g] * capacities[j]

    # Calculate the total expected occupancy at the end of the day
    total_expected_occupancy = sum(expected_occupancy)

    return total_expected_occupancy

