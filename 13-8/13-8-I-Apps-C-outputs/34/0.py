
def is_cleaning_possible(wells, pipes):
    # Initialize a dictionary to keep track of the number of robots at each well
    robots_at_well = {}
    for well in wells:
        robots_at_well[well] = 0

    # Iterate over the pipes and check if it is possible to clean all intersections
    for pipe in pipes:
        well, x, y = pipe
        if robots_at_well[well] == 2:
            return "impossible"
        robots_at_well[well] += 1

    return "possible"

