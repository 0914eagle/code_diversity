
def solve(N, L, pairs):
    # Initialize a dictionary to keep track of the items and their corresponding drawers
    items = {}
    for i in range(N):
        items[i+1] = pairs[i]
    
    # Initialize a list to keep track of the items that are stored successfully
    stored = []
    
    # Iterate through the items and apply the rules to store them
    for i in range(N):
        item = items[i+1]
        drawer1, drawer2 = item[0], item[1]
        if drawer1 not in stored:
            stored.append(drawer1)
            items[i+1] = (drawer1, drawer2)
        elif drawer2 not in stored:
            stored.append(drawer2)
            items[i+1] = (drawer2, drawer1)
        else:
            stored.append(i+1)
    
    # Return the list of items that are stored successfully
    return stored

