
def solve(n, cafes):
    # Initialize a dictionary to store the last visit of each cafe
    last_visit = {}
    
    # Iterate through the list of cafes
    for cafe in cafes:
        # If the cafe is not in the dictionary, add it to the dictionary with the current index
        if cafe not in last_visit:
            last_visit[cafe] = n
        # If the cafe is already in the dictionary, update its last visit index
        else:
            last_visit[cafe] = n
    
    # Find the cafe with the minimum last visit index
    min_last_visit = min(last_visit.values())
    
    # Return the cafe with the minimum last visit index
    return [cafe for cafe, index in last_visit.items() if index == min_last_visit][0]

