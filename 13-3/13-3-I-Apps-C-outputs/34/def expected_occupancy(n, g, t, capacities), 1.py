
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of each group size
    probabilities = [i/g for i in range(1, g+1)]

    # Calculate the expected number of people in the restaurant at the end of each hour
    expected_occupancy = [0] * (t+1)
    for i in range(t):
        # Calculate the number of people arriving in the current hour
        num_arriving = sum(probabilities)

        # Calculate the number of people leaving in the current hour
        num_leaving = expected_occupancy[i] - num_arriving

        # Calculate the number of people remaining in the restaurant at the end of the hour
        expected_occupancy[i+1] = expected_occupancy[i] - num_leaving

    # Return the expected occupancy at the end of the last hour
    return expected_occupancy[t]

