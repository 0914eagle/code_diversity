
def get_min_expected_duration(origin, destination, connections):
    # Initialize a dictionary to store the expected duration for each connection
    expected_durations = {}

    # Loop through each connection
    for connection in connections:
        # Get the origin, destination, departure time, standard journey time, probability of delay, and maximum delay for this connection
        origin, destination, departure_time, standard_journey_time, probability_of_delay, maximum_delay = connection

        # Calculate the expected duration for this connection
        expected_duration = standard_journey_time * (1 - probability_of_delay / 100)

        # Add the expected duration to the dictionary
        expected_durations[(origin, destination)] = expected_duration

    # Initialize a list to store the optimal itinerary
    itinerary = []

    # Set the current origin to the origin of the first connection
    current_origin = origin

    # Loop until the destination is reached
    while current_origin != destination:
        # Get the connection with the minimum expected duration from the current origin
        min_expected_duration = float('inf')
        min_connection = None
        for connection in expected_durations:
            if connection[0] == current_origin and expected_durations[connection] < min_expected_duration:
                min_expected_duration = expected_durations[connection]
                min_connection = connection

        # Add the minimum connection to the itinerary
        itinerary.append(min_connection)

        # Update the current origin to the destination of the minimum connection
        current_origin = min_connection[1]

    # Calculate the total expected duration of the itinerary
    total_expected_duration = sum([expected_durations[connection] for connection in itinerary])

    # Return the total expected duration
    return total_expected_duration

