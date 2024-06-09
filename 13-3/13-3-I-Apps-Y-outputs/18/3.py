
def solve(n, m, services):
    # Initialize a set to store the visited islands
    visited = set()
    # Add the starting island to the set
    visited.add(1)
    # Initialize a queue to store the next islands to visit
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Dequeue an island from the queue
        island = queue.pop(0)
        # If the island is the destination, return True
        if island == n:
            return "POSSIBLE"
        # Get the services that can be used to reach the island
        services_to_island = [service for service in services if service[0] == island or service[1] == island]
        # Add the services that can be used to reach the island to the queue
        queue += [service[0] if service[1] == island else service[1] for service in services_to_island]
        # Add the island to the visited set
        visited.add(island)
    # If the queue is empty and the destination island has not been visited, return False
    return "IMPOSSIBLE"

