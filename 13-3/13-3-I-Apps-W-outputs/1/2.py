
def solve(n, a):
    # Initialize the number of operations to 0
    operations = 0

    # Iterate through the array of cells
    for i in range(n):
        # Check if the current cell is free
        if a[i] == 0:
            # If the current cell is free, continue to the next cell
            continue
        # Otherwise, find the first free cell to the right of the current cell
        for j in range(i+1, n):
            # If a free cell is found, swap the data with the current cell
            if a[j] == 0:
                a[i], a[j] = a[j], a[i]
                operations += 1
                break

    # Return the number of operations required
    return operations

