
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of a group of size k arriving at time t
    def p(k, t):
        return (k / g) * (1 - (k - 1) / g) ** (t - 1)
    
    # Calculate the expected number of people in the restaurant at time t
    def E(t):
        # Initialize the expected number of people to 0
        expected = 0
        # Loop over all possible group sizes
        for k in range(1, g + 1):
            # Calculate the probability of the group arriving at time t
            prob = p(k, t)
            # Calculate the expected number of people in the restaurant after the group arrives
            expected_after = k * prob
            # Add the expected number of people to the total expected number of people
            expected += expected_after
        return expected
    
    # Calculate the expected number of people in the restaurant after t hours
    expected = 0
    for t in range(1, t + 1):
        expected += E(t)
    
    # Return the expected number of people in the restaurant after t hours
    return expected

