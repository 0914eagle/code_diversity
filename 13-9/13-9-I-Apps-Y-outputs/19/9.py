
def slugging_percentage(at_bats):
    # Initialize variables to store the number of hits and total bases
    hits = 0
    total_bases = 0

    # Iterate through the list of at-bats
    for at_bat in at_bats:
        # If the at-bat is not a walk, increment the number of hits and add the number of bases for the at-bat to the total
        if at_bat != -1:
            hits += 1
            total_bases += at_bat

    # Calculate the slugging percentage by dividing the total number of bases by the number of hits
    slugging_percentage = total_bases / hits

    # Return the slugging percentage
    return slugging_percentage

