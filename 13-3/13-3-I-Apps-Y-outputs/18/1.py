
def solve(n, m, services):
    # Initialize a set to store the visited islands
    visited = set()
    # Add the starting island to the set
    visited.add(1)
    # Iterate through the services
    for i in range(m):
        # Get the current service
        service = services[i]
        # If the current service connects an island that has not been visited, add it to the set
        if service[0] in visited and service[1] not in visited:
            visited.add(service[1])
        # If the current service connects an island that has been visited, remove it from the set
        elif service[1] in visited and service[0] not in visited:
            visited.remove(service[0])
    # Check if the destination island is in the set
    if n in visited:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

