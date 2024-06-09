
def solve(origin, destination, connections):
    # Initialize a dictionary to store the expected duration for each connection
    expected_durations = {}

    # Loop through each connection
    for connection in connections:
        # Get the origin, destination, departure time, standard journey time, probability of delays, and maximum delay for this connection
        origin, destination, departure_time, standard_journey_time, probability_of_delays, maximum_delay = connection

        # Calculate the expected duration for this connection
        expected_duration = standard_journey_time * (1 - probability_of_delays / 100) + maximum_delay

        # Add the expected duration to the dictionary with the key being the origin and destination
        expected_durations[(origin, destination)] = expected_duration

    # Initialize a variable to store the minimum expected duration
    minimum_expected_duration = float('inf')

    # Loop through each connection
    for connection in connections:
        # Get the origin, destination, departure time, and standard journey time for this connection
        origin, destination, departure_time, standard_journey_time = connection

        # Check if the destination is reachable from the current origin
        if destination in expected_durations:
            # Calculate the total expected duration by adding the standard journey time and the expected duration for the destination
            total_expected_duration = standard_journey_time + expected_durations[destination]

            # Update the minimum expected duration if the total expected duration is less than the current minimum
            if total_expected_duration < minimum_expected_duration:
                minimum_expected_duration = total_expected_duration

    # Return the minimum expected duration or "IMPOSSIBLE" if the destination is not reachable
    return minimum_expected_duration if minimum_expected_duration < float('inf') else "IMPOSSIBLE"

