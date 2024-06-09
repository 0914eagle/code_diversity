
def solve(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the left and right indices for each splitter
    l, r = [], []
    # Create a queue to store the indices of the splitters
    queue = [0]
    # Loop until the queue is empty
    while queue:
        # Dequeue the current splitter index
        curr = queue.pop(0)
        # If the current splitter is the last splitter, break the loop
        if curr == n:
            break
        # Increment the number of splitters
        n += 1
        # Calculate the ratio of the current splitter
        ratio = a * (c + d) // (a + b)
        # Calculate the left and right indices for the current splitter
        l_curr = (curr * a) // (a + b)
        r_curr = (curr * b) // (a + b)
        # Add the left and right indices to the list
        l.append(l_curr)
        r.append(r_curr)
        # If the left index is not -1 or -2, enqueue it
        if l_curr != -1 and l_curr != -2:
            queue.append(l_curr)
        # If the right index is not -1 or -2, enqueue it
        if r_curr != -1 and r_curr != -2:
            queue.append(r_curr)
    # Return the number of splitters and the left and right indices
    return n, l, r

