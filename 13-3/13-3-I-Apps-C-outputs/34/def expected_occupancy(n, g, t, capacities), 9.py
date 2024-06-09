
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of a group of size k arriving at time t
    def p(k, t):
        return (k / g) * (1 - (k - 1) / g) ** (t - 1)
    
    # Calculate the expected number of people in the restaurant at time t
    def E(t):
        return sum(p(k, t) * k for k in range(1, g + 1))
    
    # Calculate the expected number of people in the restaurant at the end of the day
    return sum(E(t) for t in range(1, t + 1))

