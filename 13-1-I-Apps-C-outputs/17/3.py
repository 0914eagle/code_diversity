
def solve(n, m, k, o, c, graph):
    # Initialize a set to store the cells with iron ore
    iron_ore_cells = set()
    # Initialize a set to store the cells with coal
    coal_cells = set()
    # Initialize a set to store the cells that are claimed
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

    # If there are no cells with iron ore or coal, return "impossible"
    if not iron_ore_cells and not coal_cells:
        return "impossible"

    # Loop through the graph
    for cell in range(1, n + 1):
        # If the cell is not already claimed and is not in the set of cells with iron ore or coal, claim it and add it to the set of claimed cells
        if cell not in claimed_cells and cell not in iron_ore_cells and cell not in coal_cells:
            claimed_cells.add(cell)
            min_settlers += 1

    # Return the minimum number of settlers needed
    return min_settlers

