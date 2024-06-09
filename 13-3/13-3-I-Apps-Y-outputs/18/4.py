
def solve(n, m, a, b):
    # Initialize a set to store the visited islands
    visited = set()
    # Add the starting island to the set
    visited.add(1)
    # Initialize a queue to store the next islands to visit
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Get the current island from the queue
        current = queue.pop(0)
        # If the current island is the destination, return True
        if current == n:
            return "POSSIBLE"
        # Add the current island to the set of visited islands
        visited.add(current)
        # Get the next islands to visit by finding the islands that are connected to the current island
        next_islands = [island for island in range(1, n + 1) if (current, island) in a]
        # Add the next islands to the queue
        queue += next_islands
    # If the queue is empty and the destination island has not been visited, return False
    return "IMPOSSIBLE"

