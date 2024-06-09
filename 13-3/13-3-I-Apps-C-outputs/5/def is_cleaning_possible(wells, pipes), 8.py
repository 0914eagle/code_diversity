
def is_cleaning_possible(wells, pipes):
    # Initialize a dictionary to keep track of the wells and their pipes
    well_pipes = {}
    for well in wells:
        well_pipes[well] = []

    # Add the pipes to the dictionary
    for pipe in pipes:
        well_pipes[pipe[0]].append(pipe)

    # Check if it is possible to clean all intersections
    for well in well_pipes:
        if len(well_pipes[well]) > 2:
            return "impossible"

    return "possible"

