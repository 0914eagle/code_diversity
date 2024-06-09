
def calculate_slugging_percentage(at_bats):
    # Initialize variables to keep track of hits and walks
    hits = 0
    walks = 0
    
    # Iterate through the list of at-bats
    for at_bat in at_bats:
        # If the at-bat is a hit, increase the number of hits by 1
        if at_bat > 0:
            hits += 1
        # If the at-bat is a walk, increase the number of walks by 1
        elif at_bat == -1:
            walks += 1
    
    # Calculate the slugging percentage
    slugging_percentage = (hits + walks) / (len(at_bats) - walks)
    
    # Return the slugging percentage
    return slugging_percentage

