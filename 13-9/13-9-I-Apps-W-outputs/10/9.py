
def count_simple_loops(stations, connections):
    # Initialize a dictionary to store the simple loops
    simple_loops = {}

    # Iterate over each connection
    for connection in connections:
        # Extract the source and destination stations
        source, destination = connection

        # Check if the source station is already in a simple loop
        if source in simple_loops:
            # If it is, check if the destination station is already in the simple loop
            if destination in simple_loops[source]:
                # If it is, skip this connection
                continue
            # If it's not, add the destination station to the simple loop
            simple_loops[source].add(destination)
        # If the source station is not in a simple loop, create a new simple loop with the source and destination stations
        else:
            simple_loops[source] = {source, destination}

    # Return the number of unique simple loops
    return len(simple_loops)

