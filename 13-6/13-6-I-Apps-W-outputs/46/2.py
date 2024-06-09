
def solve(n, a):
    # Sort the array to group similar colors together
    a.sort()

    # Initialize variables to keep track of the current color and the number of operations
    current_color = a[0]
    op_count = 0

    # Iterate through the array
    for i in range(1, n):
        # If the current color is different from the previous color, we need to perform an operation
        if a[i] != current_color:
            op_count += 1
            current_color = a[i]

    return op_count

