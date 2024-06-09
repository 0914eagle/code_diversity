
def solve(N, tickets):
    # Initialize a dictionary to store the minimum toll for each exit
    min_tolls = {}
    for exit, entrance in tickets:
        # If the exit is not in the dictionary, add it with the minimum toll
        if exit not in min_tolls:
            min_tolls[exit] = entrance
        # Otherwise, update the minimum toll if the current entrance is less than the previous minimum toll
        else:
            min_tolls[exit] = min(min_tolls[exit], entrance)
    
    # Calculate the total toll by summing the absolute differences between the exits and their minimum tolls
    total_toll = sum(abs(exit - min_tolls[exit]) for exit in min_tolls)
    return total_toll

