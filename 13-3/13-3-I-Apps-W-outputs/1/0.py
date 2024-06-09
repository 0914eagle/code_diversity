
def solve(n, a):
    # Initialize the number of operations to 0
    operations = 0

    # Iterate through the array of cells
    for i in range(n):
        # If the current cell is occupied by a process
        if a[i] != 0:
            # Find the first free cell before the current cell
            for j in range(i):
                if a[j] == 0:
                    # Swap the data between the current cell and the free cell
                    a[j] = a[i]
                    a[i] = 0
                    operations += 1
                    break

    # Return the number of operations
    return operations

