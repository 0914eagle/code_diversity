
def solve(n, a):
    # Initialize variables
    processes = {}
    free_cells = []
    allocated_cells = []
    operations = 0

    # Iterate through the input array
    for i in range(n):
        if a[i] == 0:
            # If the cell is free, add it to the list of free cells
            free_cells.append(i)
        else:
            # If the cell is allocated, add it to the list of allocated cells and map the process number to the cell number
            allocated_cells.append(i)
            processes[a[i]] = i

    # Sort the allocated cells in ascending order
    allocated_cells.sort()

    # Iterate through the allocated cells and find the first cell that is not in its correct position
    for i in range(len(allocated_cells)):
        if allocated_cells[i] != i:
            # If the cell is not in its correct position, find the first free cell to the right of the allocated cell
            for j in range(i, len(allocated_cells)):
                if allocated_cells[j] in free_cells:
                    # If a free cell is found, move the allocated cell to that position and update the process mapping
                    free_cells.remove(allocated_cells[j])
                    processes[a[allocated_cells[i]]] = allocated_cells[j]
                    allocated_cells[j] = allocated_cells[i]
                    allocated_cells[i] = a[allocated_cells[i]]
                    operations += 1
                    break

    return operations

