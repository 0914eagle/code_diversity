
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of a group of size k arriving at time t
    def p(k, t):
        return (k / g) * (1 - (k - 1) / g) ** (t - 1)
    
    # Calculate the expected number of people in the restaurant at time t
    def E(t):
        return sum(c * p(c, t) for c in capacities)
    
    # Calculate the expected number of people in the restaurant after t hours
    return sum(E(t + 1) * p(c, t) for c in capacities)

