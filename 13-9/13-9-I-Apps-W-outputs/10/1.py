
def count_simple_loops(transit_system):
    # Initialize a set to store the unique simple loops
    simple_loops = set()

    # Iterate over each connection in the transit system
    for connection in transit_system:
        # Check if the connection is a valid simple loop
        if is_valid_simple_loop(connection, transit_system):
            # Add the simple loop to the set of unique simple loops
            simple_loops.add(connection)

    # Return the number of unique simple loops
    return len(simple_loops)

def is_valid_simple_loop(connection, transit_system):
    # Initialize a set to store the visited stations
    visited_stations = set()

    # Initialize the current station as the first station in the connection
    current_station = connection[0]

    # Iterate until the current station is the first station in the connection
    while current_station != connection[1]:
        # Add the current station to the set of visited stations
        visited_stations.add(current_station)

        # Get the next station in the connection
        next_station = get_next_station(current_station, transit_system)

        # Check if the next station is valid
        if next_station not in transit_system:
            # The connection is not valid
            return False

        # Update the current station to the next station
        current_station = next_station

    # Check if all stations in the connection have been visited
    if len(visited_stations) != len(connection):
        # The connection is not valid
        return False

    # The connection is valid
    return True

def get_next_station(current_station, transit_system):
    # Get the list of connections from the current station
    connections = transit_system[current_station]

    # Check if there is only one connection from the current station
    if len(connections) == 1:
        # Return the next station
        return connections[0]

    # There are multiple connections from the current station
    # Find the connection that is not the current station
    for connection in connections:
        if connection != current_station:
            # Return the next station
            return connection

    # The connection is not valid
    return None

