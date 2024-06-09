
def solve(tickets):
    # Initialize a dictionary to store the minimum toll for each exit
    min_tolls = {}
    for entrance, exit in tickets:
        # If the exit is not in the dictionary, add it with the current toll
        if exit not in min_tolls:
            min_tolls[exit] = abs(entrance - exit)
        # If the exit is already in the dictionary, compare the current toll with the minimum toll
        else:
            min_tolls[exit] = min(min_tolls[exit], abs(entrance - exit))
    
    # Return the sum of the minimum tolls for all exits
    return sum(min_tolls.values())

