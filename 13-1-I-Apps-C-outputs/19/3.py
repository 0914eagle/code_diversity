
def solve(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the left and right indices for each splitter
    l = [-1] * 200
    r = [-1] * 200
    # Initialize the global input and output indices
    input_idx = 0
    output_idx_1 = -1
    output_idx_2 = -2
    # While there are still boxes to be distributed
    while c > 0 or d > 0:
        # If the global input has boxes and the current splitter has space
        if c > 0 and n < 200 and l[n] == -1:
            # Connect the global input to the current splitter
            l[n] = input_idx
            # Update the number of splitters
            n += 1
        # If the current splitter has boxes and the first output has space
        if c > 0 and n < 200 and r[n] == -1:
            # Connect the current splitter to the first output
            r[n] = output_idx_1
            # Update the number of boxes in the first output
            c -= a
        # If the current splitter has boxes and the second output has space
        if d > 0 and n < 200 and r[n] == -2:
            # Connect the current splitter to the second output
            r[n] = output_idx_2
            # Update the number of boxes in the second output
            d -= b
        # If the current splitter is full
        if l[n] != -1 and r[n] != -1 and r[n] != -2:
            # Update the global input index
            input_idx = n
            # Reset the current splitter
            l[n] = -1
            r[n] = -1
            # Decrement the number of splitters
            n -= 1
    # Return the number of splitters and the left and right indices for each splitter
    return n, l, r

