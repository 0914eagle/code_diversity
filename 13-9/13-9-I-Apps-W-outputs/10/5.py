
def count_simple_loops(transit_system):
    # Initialize a set to store the unique simple loops
    unique_loops = set()

    # Iterate over each connection in the transit system
    for i in range(len(transit_system)):
        for j in range(i+1, len(transit_system)):
            # Check if there is a direct connection from station i to station j
            if transit_system[i] == transit_system[j]:
                # Add the loop to the set of unique simple loops
                unique_loops.add(tuple(transit_system[i:j+1]))

    # Return the number of unique simple loops
    return len(unique_loops)

