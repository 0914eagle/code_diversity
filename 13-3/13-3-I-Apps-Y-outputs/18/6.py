
def solve(n, m, services):
    # Initialize a set to store the visited islands
    visited = set()
    # Add the starting island to the set
    visited.add(1)
    # Iterate through the services
    for i in range(m):
        # Get the current service
        a, b = services[i]
        # If the current service connects an island that has not been visited, add it to the set
        if a in visited and b not in visited:
            visited.add(b)
        elif a not in visited and b in visited:
            visited.add(a)
    # Check if the destination island has been visited
    if n in visited:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

