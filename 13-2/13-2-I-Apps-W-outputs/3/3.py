
def solve(r, n, reclaimed_cells):
    # Initialize a set to store the reclaimed cells
    reclaimed = set(reclaimed_cells)
    # Initialize a set to store the cells that are not allowed to be reclaimed
    not_allowed = set()
    # Loop through the reclaimed cells
    for cell in reclaimed:
        # Get the row and column of the cell
        row, col = cell
        # Add the cells that are not allowed to be reclaimed to the set
        not_allowed.add((row - 1, 3 - col))
        not_allowed.add((row, 3 - col))
        not_allowed.add((row + 1, 3 - col))
    # Check if there are any cells that are not allowed to be reclaimed and are not already reclaimed
    if any(cell in not_allowed for cell in reclaimed):
        return "LOSE"
    else:
        return "WIN"

