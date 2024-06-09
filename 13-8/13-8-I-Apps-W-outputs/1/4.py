
def check_zombie_lair(contamination_levels):
    # Initialize a set to store the possible sizes of the lair
    lair_sizes = set()
    
    # Iterate over the contamination levels
    for level in contamination_levels:
        # Check if the level is valid (between 0 and 4)
        if not (0 <= level <= 4):
            return "No"
        
        # If the level is 0, it means that the cell is not inside the lair, so we can ignore it
        if level == 0:
            continue
        
        # If the level is 1, 2 or 3, it means that the cell is on the border of the lair, so we can add the corresponding size to the set of possible sizes
        if level in [1, 2, 3]:
            lair_sizes.add(level)
    
    # Check if there is only one possible size for the lair
    if len(lair_sizes) != 1:
        return "No"
    
    # If there is only one possible size, it means that the lair is rectangular and has a non-zero area
    return "Yes"

