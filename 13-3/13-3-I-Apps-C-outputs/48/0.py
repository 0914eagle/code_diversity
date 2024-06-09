
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
    minimum_expected_duration = float('inf')

    # Loop through each connection
    for connection in connections:
        # Get the origin, destination, departure time, and standard journey time for this connection
        origin, destination, departure_time, standard_journey_time = connection

        # If the destination is the same as the origin, skip this connection
        if origin == destination:
            continue

        # If the destination is not reachable from the origin, return "IMPOSSIBLE"
        if destination not in expected_durations:
            return "IMPOSSIBLE"

        # Calculate the total expected duration for this connection
        total_expected_duration = expected_durations[connection] + expected_durations[destination]

        # If the total expected duration is less than the minimum expected duration, update the minimum expected duration
        if total_expected_duration < minimum_expected_duration:
            minimum_expected_duration = total_expected_duration

    # Return the minimum expected duration
    return minimum_expected_duration

