
def is_cleaning_possible(wells, pipes):
    # Initialize a dictionary to keep track of the wells and their pipes
    wells_dict = {}
    for well in wells:
        wells_dict[well] = []

    # Add the pipes to the dictionary
    for pipe in pipes:
        wells_dict[pipe[0]].append(pipe)

    # Check if there are any intersections
    for well in wells_dict:
        if len(wells_dict[well]) > 2:
            return "impossible"

    # Check if there are any pipes that don't intersect with any other pipe
    for well in wells_dict:
        if len(wells_dict[well]) == 1:
            return "impossible"

    # If all conditions are met, return "possible"
    return "possible"

