
def count_simple_loops(transit_system):
    # Initialize a set to store the simple loops
    simple_loops = set()

    # Iterate over each connection in the transit system
    for connection in transit_system:
        # Extract the source and destination stations from the connection
        source, destination = connection

        # Check if the destination station is already in the simple loop
        if destination in simple_loops:
            # If it is, add the source station to the simple loop
            simple_loops.add(source)
        else:
            # If it's not, create a new simple loop with the source and destination stations
            simple_loops.add(source)
            simple_loops.add(destination)

    # Return the number of unique simple loops
    return len(simple_loops)

