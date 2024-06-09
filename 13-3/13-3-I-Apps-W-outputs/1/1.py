
def defragment(memory, processes):
    # Initialize variables
    free_cells = []
    occupied_cells = []
    operations = 0

    # Separate free and occupied cells
    for cell in memory:
        if cell == 0:
            free_cells.append(cell)
        else:
            occupied_cells.append(cell)

    # Sort occupied cells in increasing order
    occupied_cells.sort()

    # Iterate through occupied cells and move them to the left
    for i in range(len(occupied_cells)):
        current_cell = occupied_cells[i]
        if i == 0:
            continue
        previous_cell = occupied_cells[i - 1]
        if current_cell != previous_cell + 1:
            operations += 1
            free_cells.append(current_cell)
            occupied_cells[i] = 0

    return operations

