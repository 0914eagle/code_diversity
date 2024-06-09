
def is_cleaning_possible(wells, pipes):
    # Initialize a dictionary to store the number of robots at each well
    robots_at_well = {well: 0 for well in wells}

    # Iterate over the pipes
    for pipe in pipes:
        # Get the well at which the pipe starts
        well = pipe[0]

        # Increment the number of robots at the well
        robots_at_well[well] += 1

        # If the number of robots at the well is greater than 1, return "impossible"
        if robots_at_well[well] > 1:
            return "impossible"

    # If all pipes have been processed and no "impossible" condition has been reached, return "possible"
    return "possible"

