
def solve(n, a):
    # Convert the list of colors to a list of indices of the same color
    indices = [[] for _ in range(21)]
    for i in range(n):
        indices[a[i]].append(i)

    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Loop through each color
    for i in range(1, 21):
        # Check if there are at least two indices with the current color
        if len(indices[i]) >= 2:
            # Find the leftmost and rightmost indices with the current color
            left = indices[i][0]
            right = indices[i][-1]

            # Calculate the number of operations needed to move the leftmost index to the rightmost position
            operations = right - left

            # Add the number of operations to the minimum number of operations
            min_operations += operations

    # Return the minimum number of operations
    return min_operations

