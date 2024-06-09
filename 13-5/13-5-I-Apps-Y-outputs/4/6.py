
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
        drawer1, drawer2 = item[0], item[1]
        
        # If the first drawer is empty, store the item in that drawer
        if drawer1 not in stored_items:
            stored_items.append(drawer1)
            continue
        
        # If the second drawer is empty, store the item in that drawer
        if drawer2 not in stored_items:
            stored_items.append(drawer2)
            continue
        
        # Try to move the item from the first drawer to its other drawer
        other_drawer = 3 - drawer1
        if other_drawer not in stored_items:
            stored_items.append(other_drawer)
            continue
        
        # Try to move the item from the second drawer to its other drawer
        other_drawer = 3 - drawer2
        if other_drawer not in stored_items:
            stored_items.append(other_drawer)
            continue
        
        # If all else fails, throw away the item
        stored_items.append("SMECE")
    
    # Return the list of stored items
    return stored_items

