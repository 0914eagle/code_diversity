
def get_min_expected_duration(origin, destination, connections):
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
    min_expected_duration = float("inf")

    # Loop through each connection
    for connection in connections:
        # Get the origin, destination, departure time, and standard journey time for this connection
        origin, destination, departure_time, standard_journey_time = connection

        # If the destination is the same as the input destination, calculate the minimum expected duration for this connection
        if destination == destination:
            # Calculate the minimum expected duration for this connection
            min_expected_duration = min(min_expected_duration, expected_durations[connection])

        # If the destination is not the input destination, calculate the minimum expected duration for this connection and the next connection
        else:
            # Get the next connection in the itinerary
            next_connection = connections[connections.index(connection) + 1]

            # Calculate the minimum expected duration for this connection and the next connection
            min_expected_duration = min(min_expected_duration, expected_durations[connection] + expected_durations[next_connection])

    # Return the minimum expected duration
    return min_expected_duration

