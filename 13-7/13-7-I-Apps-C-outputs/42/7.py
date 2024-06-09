
def max_flowers(field, start_row, start_col):
    # Initialize a queue to store the next positions to visit
    queue = [(start_row, start_col)]
    # Initialize a set to keep track of the visited positions
    visited = set()
    # Initialize a variable to store the maximum number of flowers visited
    max_flowers = 0

    # Loop until the queue is empty
    while queue:
        # Get the current position from the queue
        row, col = queue.pop(0)
        # If the current position is not visited, mark it as visited and add it to the set
        if (row, col) not in visited:
            visited.add((row, col))
            # Get the number of petals at the current position
            num_petals = field[row - 1][col - 1]
            # If the number of petals is greater than the maximum number of flowers visited so far, update the maximum number of flowers visited
            if num_petals > max_flowers:
                max_flowers = num_petals
            # Add the adjacent positions to the queue
            if row > 1:
                queue.append((row - 1, col))
            if row < len(field):
                queue.append((row + 1, col))
            if col > 1:
                queue.append((row, col - 1))
            if col < len(field[0]):
                queue.append((row, col + 1))

    return max_flowers

