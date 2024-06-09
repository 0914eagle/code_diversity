
def solve(N, L, pairs):
    # Initialize a dictionary to store the items and their corresponding drawers
    items = {}
    for i in range(N):
        items[i+1] = pairs[i]
    
    # Initialize a list to store the items that will be stored
    stored_items = []
    
    # Iterate through the items and apply the rules to determine where they will be stored
    for i in range(N):
        item = items[i+1]
        drawer_a, drawer_b = item
        if drawer_a not in stored_items:
            stored_items.append(drawer_a)
            items[i+1] = (drawer_a, drawer_b)
        elif drawer_b not in stored_items:
            stored_items.append(drawer_b)
            items[i+1] = (drawer_a, drawer_b)
        else:
            stored_items.append(item)
    
    # Return the list of items that will be stored
    return stored_items
