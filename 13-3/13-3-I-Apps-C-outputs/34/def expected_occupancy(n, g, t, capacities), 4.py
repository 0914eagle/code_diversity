
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of a group of size k occupying a table
    probabilities = [0] * (g + 1)
    for k in range(1, g + 1):
        probabilities[k] = (k / g) ** (n - 1) * (1 - (k / g) ** n)
    
    # Calculate the expected number of people in the restaurant at the end of each hour
    expected_occupancy = [0] * (t + 1)
    for i in range(1, t + 1):
        for k in range(1, g + 1):
            expected_occupancy[i] += probabilities[k] * k
    
    # Calculate the total expected occupancy at the end of the day
    total_expected_occupancy = 0
    for i in range(1, t + 1):
        total_expected_occupancy += expected_occupancy[i]
    
    return total_expected_occupancy

