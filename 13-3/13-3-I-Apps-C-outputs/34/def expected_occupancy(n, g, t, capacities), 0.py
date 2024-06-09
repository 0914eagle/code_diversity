
def expected_occupancy(n, g, t, capacities):
    # Calculate the probability of a group of size k arriving in the next hour
    probabilities = [(k / g) for k in range(1, g + 1)]

    # Initialize the expected occupancy to 0
    expected_occupancy = 0

    # Loop through each hour
    for hour in range(t):
        # Loop through each table
        for i in range(n):
            # Calculate the probability of the table being occupied in this hour
            prob_occupied = probabilities[i]

            # Calculate the expected number of people in the table in this hour
            expected_people = capacities[i] * prob_occupied

            # Add the expected number of people to the total expected occupancy
            expected_occupancy += expected_people

    # Return the expected occupancy
    return expected_occupancy

