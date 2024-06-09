
def solve(n, a):
    # Initialize variables
    processes = {}
    free_cells = []
    occupied_cells = []
    moves = 0

    # Separate the cells into free and occupied lists
    for i in range(n):
        if a[i] == 0:
            free_cells.append(i)
        else:
            if a[i] not in processes:
                processes[a[i]] = [i]
            else:
                processes[a[i]].append(i)

    # Sort the occupied cells by process number
    for process in processes:
        processes[process].sort()

    # Move the occupied cells to the beginning of the memory
    for process in processes:
        for cell in processes[process]:
            if cell not in free_cells:
                moves += 1
                free_cells.append(cell)
                occupied_cells.append(cell)

    # Move the remaining free cells to the end of the memory
    for cell in free_cells:
        if cell not in occupied_cells:
            moves += 1
            free_cells.append(cell)

    return moves

