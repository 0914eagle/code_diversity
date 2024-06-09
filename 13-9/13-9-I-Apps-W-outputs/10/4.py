
def count_simple_loops(transit_system):
    # Initialize a set to store the simple loops
    simple_loops = set()

    # Iterate over each connection in the transit system
    for i in range(len(transit_system)):
        # Get the current connection
        current_connection = transit_system[i]

        # Check if the current connection is a simple loop
        if current_connection[0] == current_connection[1]:
            # If it is a simple loop, add it to the set of simple loops
            simple_loops.add(current_connection)

    # Return the number of unique simple loops in the transit system
    return len(simple_loops)

