
def is_possible(wells, pipes):
    # Initialize a set to store the wells that have been cleaned
    cleaned_wells = set()

    # Iterate over the pipes
    for pipe in pipes:
        # If the well at which the pipe starts has not been cleaned yet, clean it
        if pipe[0] not in cleaned_wells:
            cleaned_wells.add(pipe[0])

        # If the well at which the pipe ends has not been cleaned yet, clean it
        if pipe[1] not in cleaned_wells:
            cleaned_wells.add(pipe[1])

    # If all wells have been cleaned, return "possible"
    if len(cleaned_wells) == len(wells):
        return "possible"
    else:
        return "impossible"

