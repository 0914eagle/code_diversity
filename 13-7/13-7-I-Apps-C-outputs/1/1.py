
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time to -1
    min_time = -1

    # Create a set to store the visited states
    visited = set()

    # Create a queue to store the states to be visited
    queue = [(h1, h2)]

    # Loop until the queue is empty
    while queue:
        # Get the current state from the queue
        h1, h2 = queue.pop(0)

        # If the current state is the target state, return the minimum time
        if h1 == a1 and h2 == a2:
            return min_time

        # If the current state is not in the visited set, add it to the visited set and enqueue its neighbors
        if (h1, h2) not in visited:
            visited.add((h1, h2))

            # Enqueue the left neighbor
            queue.append(((h1 * x1 + y1) % m, h2))

            # Enqueue the right neighbor
            queue.append((h1, (h2 * x2 + y2) % m))

            # Increment the minimum time
            min_time += 1

    # If the queue is empty and the target state is not reached, return -1
    return -1

