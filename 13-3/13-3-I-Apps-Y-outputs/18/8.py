
def is_possible(n, m, services):
    # Initialize a set to store the islands that can be reached by the first service
    reachable_islands = set()
    for service in services:
        # If the first service can reach the destination island, return "POSSIBLE"
        if service[1] == n:
            return "POSSIBLE"
        # Add the island that can be reached by the first service to the set
        reachable_islands.add(service[1])
    # If the set is empty, return "IMPOSSIBLE"
    if not reachable_islands:
        return "IMPOSSIBLE"
    # Iterate through the services again
    for service in services:
        # If the second service can reach an island that is not in the set, return "IMPOSSIBLE"
        if service[0] not in reachable_islands:
            return "IMPOSSIBLE"
        # If the second service can reach the destination island, return "POSSIBLE"
        if service[1] == n:
            return "POSSIBLE"
    # If the function reaches this point, it means that there is no way to reach the destination island by using two boat services, so return "IMPOSSIBLE"
    return "IMPOSSIBLE"

