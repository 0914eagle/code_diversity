
def solve(n, a):
    # Sort the array to group similar colors together
    a.sort()

    # Initialize variables to keep track of the current color and the number of operations
    current_color = a[0]
    num_operations = 0

    # Iterate through the array and check if the current color is the same as the previous color
    for i in range(1, n):
        if a[i] != current_color:
            # If the colors are different, increment the number of operations
            num_operations += 1
            current_color = a[i]

    # Return the number of operations required to rearrange the marbles
    return num_operations

