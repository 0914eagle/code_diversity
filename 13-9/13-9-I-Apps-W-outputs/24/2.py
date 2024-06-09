
def find_last_visited_cafe(n, a):
    # Initialize a dictionary to store the last visit of each cafe
    last_visited = {}
    
    # Iterate through the list of visited cafes
    for cafe in a:
        # If the cafe is not in the dictionary, add it to the dictionary with the current index
        if cafe not in last_visited:
            last_visited[cafe] = len(a) - 1
        # Otherwise, update the last visit of the cafe if the current index is later than the previous one
        else:
            last_visited[cafe] = max(last_visited[cafe], len(a) - 1)
    
    # Find the cafe with the latest last visit
    latest_last_visit = max(last_visited.values())
    
    # Find the cafe with the latest last visit that is also the latest visit to any other cafe
    for cafe, visit in last_visited.items():
        if visit == latest_last_visit:
            return cafe
    
    # If no cafe has the latest last visit to any other cafe, return the cafe with the latest last visit
    return max(last_visited, key=last_visited.get)

