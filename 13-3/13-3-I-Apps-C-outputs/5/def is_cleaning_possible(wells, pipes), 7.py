
def is_cleaning_possible(wells, pipes):
    # Initialize a dictionary to keep track of the wells and their positions
    wells_dict = {}
    for well in wells:
        wells_dict[well[0]] = (well[1], well[2])

    # Initialize a list to keep track of the pipes and their endpoints
    pipes_list = []
    for pipe in pipes:
        pipes_list.append((pipe[0], (pipe[1], pipe[2])))

    # Initialize a set to keep track of the intersections
    intersections = set()

    # Iterate over the pipes and find the intersections
    for pipe in pipes_list:
        for well in wells_dict:
            if well != pipe[0] and wells_dict[well] == pipe[1]:
                intersections.add(well)

    # Check if all intersections have at most one robot
    for intersection in intersections:
        if len([pipe for pipe in pipes_list if pipe[0] == intersection]) > 1:
            return "impossible"

    return "possible"

