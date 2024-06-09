
def solve(n, path):
    # Initialize a list to store the path
    router_path = [1]

    # Iterate through the path
    for i in range(1, n):
        # Find the next router in the path
        next_router = path[i-1]

        # Check if the next router is already in the path
        if next_router in router_path:
            # If it is, find the first router that is not in the path
            for j in range(1, n+1):
                if j not in router_path:
                    next_router = j
                    break

        # Add the next router to the path
        router_path.append(next_router)

    return router_path

