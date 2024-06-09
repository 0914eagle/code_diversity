
def count_simple_loops(transit_system):
    # Initialize a dictionary to store the simple loops
    simple_loops = {}

    # Iterate over each connection in the transit system
    for connection in transit_system:
        # Extract the starting and ending stations of the connection
        start, end = connection

        # Check if the connection is a simple loop
        if start == end:
            # If the connection is a simple loop, add it to the dictionary
            simple_loops[frozenset(connection)] = 1

    # Return the number of unique simple loops in the transit system
    return len(simple_loops)

