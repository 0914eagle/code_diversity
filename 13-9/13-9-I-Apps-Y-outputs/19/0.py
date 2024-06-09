
def slugging_percentage(at_bats):
    # Initialize variables to keep track of hits and bases
    hits, bases = 0, 0
    
    # Iterate over the at-bats
    for at_bat in at_bats:
        # Check if the at-bat is not a walk
        if at_bat != -1:
            # Increment the number of hits and bases
            hits += 1
            bases += at_bat
    
    # Calculate the slugging percentage
    slugging_percentage = bases / (hits - 1)
    
    # Return the slugging percentage
    return slugging_percentage

