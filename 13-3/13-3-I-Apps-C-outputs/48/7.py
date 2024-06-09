
def solve(origin, destination, connections):
    # Initialize a dictionary to store the expected duration for each connection
    expected_durations = {}

    # Loop through each connection
    for connection in connections:
        # Get the origin, destination, departure time, standard journey time, probability of delay, and maximum delay for this connection
        origin, destination, departure_time, standard_journey_time, probability_of_delay, maximum_delay = connection

        # Calculate the expected duration for this connection
        expected_duration = standard_journey_time * (1 - probability_of_delay / 100) + maximum_delay

        # Add the expected duration to the dictionary with the connection as the key
        expected_durations[connection] = expected_duration

    # Initialize a variable to store the minimum expected duration
    minimum_expected_duration = float("inf")

    # Loop through each connection
    for connection in connections:
        # Get the origin, destination, departure time, and standard journey time for this connection
        origin, destination, departure_time, standard_journey_time = connection

        # If the destination is the same as the input destination, calculate the minimum expected duration
        if destination == destination:
            # Calculate the minimum expected duration by adding the expected duration for this connection to the expected duration for the previous connection
            minimum_expected_duration = min(minimum_expected_duration, expected_durations[connection] + expected_durations[connection - 1])

    # Return the minimum expected duration
    return minimum_expected_duration

