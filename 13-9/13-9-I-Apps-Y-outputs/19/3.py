
def slugging_percentage(at_bats):
    # Initialize variables to keep track of hits and walks
    hits = 0
    walks = 0
    
    # Iterate through the at-bats and count the number of hits and walks
    for at_bat in at_bats:
        if at_bat == 0:
            hits += 1
        elif at_bat == -1:
            walks += 1
    
    # Calculate the slugging percentage
    slugging_percentage = (hits + walks) / (len(at_bats) - walks)
    
    return slugging_percentage

