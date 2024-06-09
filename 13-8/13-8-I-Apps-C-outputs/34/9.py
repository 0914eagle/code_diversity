
def can_clean_all_intersections(wells, pipes):
    # Initialize a set to store the wells that have been cleaned
    cleaned_wells = set()
    # Iterate through the pipes
    for pipe in pipes:
        # If the well at which the pipe starts has not been cleaned yet, insert a robot into the pipe
        if pipe[0] not in cleaned_wells:
            # Insert a robot into the pipe
            cleaned_wells.add(pipe[0])
    # If all wells have been cleaned, return "possible"
    if len(cleaned_wells) == len(wells):
        return "possible"
    # Otherwise, return "impossible"
    return "impossible"

