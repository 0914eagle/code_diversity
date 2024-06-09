
def solve(n, m, services):
    # Initialize a set to store the islands that can be reached by the first service
    reachable_islands = set()
    
    # Iterate through the services
    for service in services:
        # If the first island of the service is in the reachable islands set, add the second island to the reachable islands set
        if service[0] in reachable_islands:
            reachable_islands.add(service[1])
        # If the second island of the service is in the reachable islands set, add the first island to the reachable islands set
        elif service[1] in reachable_islands:
            reachable_islands.add(service[0])
    
    # Return "POSSIBLE" if Island N is in the reachable islands set, otherwise return "IMPOSSIBLE"
    return "POSSIBLE" if n in reachable_islands else "IMPOSSIBLE"

