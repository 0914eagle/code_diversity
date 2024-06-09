
def find_last_visited_cafe(n, visits):
    # Initialize a dictionary to store the last visit of each cafe
    last_visited = {}
    
    # Iterate through the visits and update the last visited dictionary
    for visit in visits:
        if visit in last_visited:
            last_visited[visit] = n
        else:
            last_visited[visit] = n - 1
    
    # Find the cafe with the maximum last visit time
    max_last_visit = max(last_visited.values())
    
    # Find the cafe with the maximum last visit time that has not been visited yet
    for cafe, last_visit in last_visited.items():
        if last_visit == max_last_visit:
            return cafe
    
    # If no cafe has not been visited yet, return -1
    return -1

