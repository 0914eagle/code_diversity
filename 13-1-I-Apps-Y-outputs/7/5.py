
def solve(N, L, pairs):
    # Initialize a dictionary to store the items and their corresponding drawers
    items = {}
    for i in range(N):
        items[i+1] = pairs[i]
    
    # Initialize a list to store the items that will be stored
    stored_items = []
    
    # Iterate through the items and apply the rules to store them
    for i in range(N):
        item = items[i+1]
        drawer_a, drawer_b = item
        if drawer_a not in stored_items and drawer_b not in stored_items:
            # Both drawers are empty, store the item in the first drawer
            stored_items.append(item[0])
        elif drawer_a in stored_items and drawer_b not in stored_items:
            # Drawer A is occupied, store the item in drawer B
            stored_items.append(item[1])
        elif drawer_a not in stored_items and drawer_b in stored_items:
            # Drawer B is occupied, store the item in drawer A
            stored_items.append(item[0])
        else:
            # Both drawers are occupied, throw away the item
            stored_items.append("SMECE")
    
    # Return the list of stored items
    return stored_items

