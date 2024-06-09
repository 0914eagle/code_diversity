
def solve(n, m, services):
    # Initialize a set to store the visited islands
    visited = set()
    # Add the starting island to the set
    visited.add(1)
    # Initialize a queue to store the next islands to visit
    queue = [1]
    # Loop through the services
    for i in range(m):
        # Get the current island and the next island
        current, next = services[i]
        # If the next island is not in the visited set, add it to the queue
        if next not in visited:
            queue.append(next)
            # Add the next island to the visited set
            visited.add(next)
        # If the next island is the destination island, return True
        if next == n:
            return True
    # If we reach the end of the loop and the destination island is not in the visited set, return False
    return False

