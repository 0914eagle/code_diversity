
def intergalactic_surgeon(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    organs = [i for i in range(1, cols * 2 + 1)]
    empty_cell = (rows - 1, cols)
    moves = []

    # Check if the grid is valid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != "E" and grid[i][j] not in organs:
                return "SURGERY FAILED"

    # Move the organs to their correct positions
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != "E":
                current_organ = grid[i][j]
                target_cell = (i, organs.index(current_organ))
                moves.append(move_organ(grid, empty_cell, target_cell))
                empty_cell = target_cell
                organs.remove(current_organ)

    return "SURGERY COMPLETE\n" + "".join(moves)

def move_organ(grid, empty_cell, target_cell):
    # Check if the target cell is empty
    if grid[target_cell[0]][target_cell[1]] != "E":
        return ""

    # Check if the target cell is in the same row as the empty cell
    if target_cell[0] == empty_cell[0]:
        # Check if the target cell is to the left of the empty cell
        if target_cell[1] < empty_cell[1]:
            return "l"
        # Check if the target cell is to the right of the empty cell
        else:
            return "r"

    # Check if the target cell is in the same column as the empty cell
    if target_cell[1] == empty_cell[1]:
        # Check if the target cell is above the empty cell
        if target_cell[0] < empty_cell[0]:
            return "u"
        # Check if the target cell is below the empty cell
        else:
            return "d"

    # Check if the target cell is in the center of the grid
    if target_cell[0] == (empty_cell[0] + 1) // 2 and target_cell[1] == (empty_cell[1] + 1) // 2:
        # Check if the target cell is above and to the left of the empty cell
        if target_cell[0] < empty_cell[0] and target_cell[1] < empty_cell[1]:
            return "l"
        # Check if the target cell is above and to the right of the empty cell
        elif target_cell[0] < empty_cell[0] and target_cell[1] > empty_cell[1]:
            return "r"
        # Check if the target cell is below and to the left of the empty cell
        elif target_cell[0] > empty_cell[0] and target_cell[1] < empty_cell[1]:
            return "u"
        # Check if the target cell is below and to the right of the empty cell
        else:
            return "d"

    return ""

