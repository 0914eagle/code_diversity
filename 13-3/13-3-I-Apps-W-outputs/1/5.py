
def solve(n, a):
    # Initialize the number of operations to 0
    operations = 0

    # Iterate through the array of cells
    for i in range(n):
        # If the current cell is occupied by a process
        if a[i] != 0:
            # Find the first free cell before the current cell
            free_cell = i
            while free_cell > 0 and a[free_cell - 1] != 0:
                free_cell -= 1

            # If the free cell is not the current cell
            if free_cell != i:
                # Move the data from the current cell to the free cell
                a[free_cell] = a[i]
                a[i] = 0
                operations += 1

    # Return the number of operations
    return operations

