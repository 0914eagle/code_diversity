
def solve(n, m, services):
    # Initialize a set to store the visited islands
    visited = set()
    # Add the starting island to the set
    visited.add(1)
    # Iterate through the services
    for i in range(m):
        # Get the current service
        service = services[i]
        # Check if the current service connects two visited islands
        if service[0] in visited and service[1] in visited:
            # If so, return POSSIBLE
            return "POSSIBLE"
        # If the current service connects an unvisited island, add it to the set
        visited.add(service[1])
    # If we reach this point, it means that we have visited all the islands but still cannot reach the destination
    return "IMPOSSIBLE"

