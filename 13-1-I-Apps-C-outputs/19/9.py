
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
        # If the current splitter is not the last splitter, create two new splitters
        if i != n-1:
            # Increment the number of splitters
            n += 1
            # Add the indices of the new splitters to the queue
            queue.append(i)
            queue.append(n-1)
        # Add the current splitter's indices to the list
        l.append(i)
        r.append(n-1)
    # Return the number of splitters and their indices
    return n, l, r

