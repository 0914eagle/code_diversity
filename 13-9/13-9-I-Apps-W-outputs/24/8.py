
def find_unvisited_cafe(n, visits):
    # Initialize a set to store the indices of cafes visited by Vlad
    visited_cafes = set()
    # Iterate through the list of visits
    for visit in visits:
        # If the current cafe has not been visited before, add it to the set of visited cafes
        if visit not in visited_cafes:
            visited_cafes.add(visit)
    # Return the first cafe that has not been visited, which is the last unvisited cafe
    return [cafe for cafe in range(1, n+1) if cafe not in visited_cafes][0]

