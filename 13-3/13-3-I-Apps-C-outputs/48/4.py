
def solve(origin, destination, connections):
    # Initialize a dictionary to store the expected duration for each connection
    expected_durations = {}

    # Loop through each connection
    for connection in connections:
        # Extract the information for this connection
        origin, destination, departure_time, standard_duration, probability, maximum_delay = connection

        # Calculate the expected duration for this connection
        expected_duration = standard_duration * (1 - probability / 100) + maximum_delay

        # Add the expected duration to the dictionary
        expected_durations[(origin, destination)] = expected_duration

    # Initialize a list to store the optimal itinerary
    itinerary = []

    # Set the current location to the origin
    current_location = origin

    # Loop until the destination is reached
    while current_location != destination:
        # Find the connection with the minimum expected duration from the current location
        min_expected_duration = float('inf')
        min_connection = None
        for connection in expected_durations:
            if connection[0] == current_location and expected_durations[connection] < min_expected_duration:
                min_expected_duration = expected_durations[connection]
                min_connection = connection

        # Add the minimum connection to the itinerary
        itinerary.append(min_connection)

        # Update the current location to the destination of the minimum connection
        current_location = min_connection[1]

    # Calculate the total expected duration of the itinerary
    total_expected_duration = sum([expected_durations[connection] for connection in itinerary])

    # Return the total expected duration
    return total_expected_duration

