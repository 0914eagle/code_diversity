
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of a group of size k arriving at time t
    def probability(k, t):
        return (k / g) * (1 - (k - 1) / g) ** (t - 1)
    
    # Calculate the expected number of people in the restaurant at time t
    def expected_people(t):
        people = 0
        for i in range(1, g + 1):
            people += i * probability(i, t)
        return people
    
    # Calculate the expected number of people in the restaurant after t hours
    total_people = 0
    for t in range(1, t + 1):
        total_people += expected_people(t)
    
    # Return the expected number of people in the restaurant at the end of the day
    return total_people

