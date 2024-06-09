
def solve(wells, pipes):
    # Initialize a set to store the wells that have been cleaned
    cleaned_wells = set()
    
    # Iterate over the pipes
    for pipe in pipes:
        # Check if the well at the start of the pipe has already been cleaned
        if pipe[0] not in cleaned_wells:
            # If not, add it to the set of cleaned wells
            cleaned_wells.add(pipe[0])
    
    # Check if all wells have been cleaned
    if len(cleaned_wells) == len(wells):
        return "possible"
    else:
        return "impossible"

