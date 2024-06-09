
def verify_cleaning(wells, pipes):
    # Initialize a dictionary to store the number of pipes at each well
    well_pipes = {well: 0 for well in wells}

    # Iterate over the pipes and increment the number of pipes at each well
    for pipe in pipes:
        well_pipes[pipe[0]] += 1

    # Check if there is at least one well with at least two pipes
    if any(num_pipes >= 2 for num_pipes in well_pipes.values()):
        return "possible"
    else:
        return "impossible"

