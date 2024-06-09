
def solve(n, m, k, o, c, graph):
    # Initialize a set to store the cells with iron ore
    iron_ore_cells = set()
    # Initialize a set to store the cells with coal
    coal_cells = set()
    # Initialize a set to store the claimed cells
    claimed_cells = set()
    # Initialize a variable to store the minimum number of settlers needed
    min_settlers = 0

    # Loop through the cells with iron ore
    for cell in o:
        # Add the cell to the set of cells with iron ore
        iron_ore_cells.add(cell)
        # If the cell is not already claimed, claim it and add it to the set of claimed cells
        if cell not in claimed_cells:
            claimed_cells.add(cell)
            min_settlers += 1

    # Loop through the cells with coal
    for cell in c:
        # Add the cell to the set of cells with coal
        coal_cells.add(cell)
        # If the cell is not already claimed, claim it and add it to the set of claimed cells
        if cell not in claimed_cells:
            claimed_cells.add(cell)
            min_settlers += 1

    # If both sets of cells are not empty, return the minimum number of settlers needed
    if iron_ore_cells and coal_cells:
        return min_settlers
    else:
        return "impossible"

