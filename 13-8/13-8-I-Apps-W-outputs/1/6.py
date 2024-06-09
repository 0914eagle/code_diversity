
def check_lair(grid):
    # Initialize a set to store the levels of Zombie Contamination
    levels = set()
    
    # Loop through the grid and add the levels of Zombie Contamination to the set
    for row in grid:
        for level in row:
            levels.add(int(level))
    
    # Check if the set of levels contains all numbers between 0 and 4, inclusive
    return len(levels) == 5 and set(range(5)) == levels

