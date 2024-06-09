
def solve(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the left and right indices for each splitter
    l = [-1] * 200
    r = [-1] * 200
    # Set the global input to be connected to splitter 0
    l[0] = -2
    r[0] = -1
    # Loop until the global output is reached
    while l[0] != -1 or r[0] != -1:
        # If the global input is connected to a splitter
        if l[0] != -1:
            # Calculate the ratio of boxes sent to the left output
            left_ratio = a / (a + b)
            # Connect the left output of the global input to a new splitter
            l[0] = n
            r[0] = n + 1
            # Set the left output of the new splitter to be connected to the global output
            l[n] = -1
            r[n] = -2
            # Increment the number of splitters
            n += 1
        # If the global input is connected to a splitter
        if r[0] != -1:
            # Calculate the ratio of boxes sent to the right output
            right_ratio = b / (a + b)
            # Connect the right output of the global input to a new splitter
            l[0] = n
            r[0] = n + 1
            # Set the right output of the new splitter to be connected to the global output
            l[n] = -1
            r[n] = -2
            # Increment the number of splitters
            n += 1
    # Return the number of splitters and the left and right indices for each splitter
    return n, l, r

