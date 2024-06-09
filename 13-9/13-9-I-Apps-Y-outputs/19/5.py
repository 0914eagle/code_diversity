
def slugging_percentage(at_bats):
    # Initialize variables to track hits and walks
    hits = 0
    walks = 0
    
    # Iterate through the at-bats
    for at_bat in at_bats:
        # Check if the at-bat is a walk
        if at_bat == -1:
            # If it is, increment the walks count
            walks += 1
        else:
            # If it's not a walk, increment the hits count
            hits += at_bat
    
    # Calculate the slugging percentage
    slugging_percentage = hits / (len(at_bats) - walks)
    
    # Return the slugging percentage
    return slugging_percentage

