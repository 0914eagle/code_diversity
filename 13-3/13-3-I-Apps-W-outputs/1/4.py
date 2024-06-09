
def solve(n, a):
    # Initialize the number of operations to 0
    operations = 0

    # Iterate through the array of cells
    for i in range(n):
        # If the current cell is occupied by a process
        if a[i] != 0:
            # Find the index of the first free cell before the current cell
            free_index = i - 1
            while free_index >= 0 and a[free_index] != 0:
                free_index -= 1

            # If there is a free cell before the current cell
            if free_index >= 0:
                # Swap the data of the current cell with the free cell
                a[free_index], a[i] = a[i], a[free_index]
                operations += 1

    # Return the number of operations
    return operations

