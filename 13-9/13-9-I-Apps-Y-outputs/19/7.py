
def calculate_slugging_percentage(at_bats):
    # Initialize variables to keep track of bases and walks
    bases = 0
    walks = 0
    
    # Iterate through the list of at-bats
    for at_bat in at_bats:
        # If at-bat is a walk, increment walks by 1
        if at_bat == -1:
            walks += 1
        # Otherwise, increment bases by the value of the at-bat
        else:
            bases += at_bat
    
    # Calculate slugging percentage by dividing bases by number of at-bats minus walks
    slugging_percentage = bases / (len(at_bats) - walks)
    
    # Return the slugging percentage
    return slugging_percentage

