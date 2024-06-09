
def is_possible(n, m, boat_services):
    # Initialize a set to store the islands that can be reached by the first boat service
    reachable_islands = set()
    # Loop through each boat service
    for i in range(m):
        # Get the two islands connected by the current boat service
        island1, island2 = boat_services[i]
        # If the first island is 1 and the second island is not N, add the second island to the set of reachable islands
        if island1 == 1 and island2 != n:
            reachable_islands.add(island2)
        # If the second island is N, return True
        elif island2 == n:
            return True
    # If we reach the end of the loop and N is not in the set of reachable islands, return False
    return n in reachable_islands

