
def solve(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the left and right indices for each splitter
    left = [-1] * 200
    right = [-1] * 200
    # Initialize the global input and output indices
    input_index = 0
    output_indices = [-2, -1]
    # While there are still boxes to be distributed
    while c > 0 or d > 0:
        # If the global input has boxes to distribute
        if c > 0:
            # Distribute the global input over the first output
            c -= 1
            output_indices[0] += 1
        # If the global input has boxes to distribute
        if d > 0:
            # Distribute the global input over the second output
            d -= 1
            output_indices[1] += 1
        # If the number of splitters is less than the maximum allowed
        if n < 200:
            # Add a new splitter with the given ratio
            n += 1
            left[n-1] = input_index
            right[n-1] = output_indices[0]
            input_index = n-1
        # If the number of splitters is equal to the maximum allowed
        else:
            # Find the splitter with the minimum number of boxes in its input
            min_index = 0
            for i in range(1, n):
                if left[i] < left[min_index]:
                    min_index = i
            # Distribute the boxes from the minimum input splitter over the first output
            left[min_index] += 1
            output_indices[0] += 1
    # Return the number of splitters and their connections
    return n, left, right

