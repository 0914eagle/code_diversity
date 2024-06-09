
def possible_to_clean_intersections(wells, pipes):
    # Initialize a set to store the positions of the wells
    well_positions = set()
    # Add the positions of the wells to the set
    for well in wells:
        well_positions.add((well[0], well[1]))

    # Initialize a set to store the positions of the intersections
    intersection_positions = set()
    # Iterate over the pipes
    for pipe in pipes:
        # Get the start and end positions of the pipe
        start_position = (pipe[1], pipe[2])
        end_position = (pipe[3], pipe[4])
        # If the start position is a well, add it to the set of well positions
        if start_position in well_positions:
            well_positions.add(start_position)
        # If the end position is a well, add it to the set of well positions
        if end_position in well_positions:
            well_positions.add(end_position)
        # If the start and end positions are not the same, add the midpoint of the pipe to the set of intersection positions
        if start_position != end_position:
            intersection_positions.add(((start_position[0] + end_position[0]) // 2, (start_position[1] + end_position[1]) // 2))

    # If the number of intersections is equal to the number of wells, return "possible"
    if len(intersection_positions) == len(well_positions):
        return "possible"
    else:
        return "impossible"

