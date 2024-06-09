
def solve(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the left and right indices for each splitter
    l, r = [], []
    # Create a queue to store the indices of the splitters
    queue = [0]
    # Loop until the queue is empty
    while queue:
        # Dequeue an index from the queue
        i = queue.pop(0)
        # If the current splitter is not the last splitter, add a new splitter to the right
        if i != n-1:
            # Add a new splitter to the right with a ratio of a/(a+b)
            r.append(n)
            queue.append(n)
            n += 1
        # If the current splitter is not the first splitter, add a new splitter to the left
        if i != 0:
            # Add a new splitter to the left with a ratio of b/(a+b)
            l.append(n-1)
            queue.append(n-1)
            n += 1
    # Return the number of splitters and the left and right indices for each splitter
    return n, l, r

