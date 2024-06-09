
def solve(n, a):
    # Initialize the number of operations to 0
    operations = 0

    # Iterate through the array of cells
    for i in range(n):
        # Check if the current cell is free
        if a[i] == 0:
            # If the current cell is free, skip it
            continue
        # Otherwise, find the first free cell before the current cell
        first_free = i
        while first_free > 0 and a[first_free - 1] != 0:
            first_free -= 1
        # If the first free cell is before the current cell, move the data to the first free cell
        if first_free < i:
            operations += 1
            a[first_free] = a[i]
            a[i] = 0

    # Return the number of operations
    return operations

