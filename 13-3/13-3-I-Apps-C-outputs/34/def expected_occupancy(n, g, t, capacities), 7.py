
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of a group of size k occupying a table
    probabilities = [0] * (g + 1)
    for i in range(1, g + 1):
        probabilities[i] = i / g

    # Calculate the expected number of people in the restaurant after t hours
    expected_people = 0
    for i in range(t):
        # Calculate the probability that a group of size k arrives in the current hour
        group_probability = 1
        for j in range(1, g + 1):
            group_probability *= probabilities[j]

        # Calculate the expected number of people in the restaurant after the current hour
        expected_people_hour = 0
        for j in range(n):
            expected_people_hour += group_probability * capacities[j]

        # Add the expected number of people in the restaurant after the current hour to the total
        expected_people += expected_people_hour

    return expected_people

