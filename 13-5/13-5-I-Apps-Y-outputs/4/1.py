
def solve(N, L, drawers):
    # Initialize a dictionary to store the items and their corresponding drawers
    items = {}
    for i in range(N):
        items[i+1] = drawers[i]
    
    # Iterate through the items and apply the rules to store them
    for i in range(N):
        item = items[i+1]
        if item[0] not in items.values():
            items[i+1] = (item[0], None)
        elif item[1] not in items.values():
            items[i+1] = (item[1], None)
        else:
            items[i+1] = move_item(items, item)
    
    # Return the items and their corresponding drawers
    return items

def move_item(items, item):
    # If the item is already stored in a drawer, return the drawer
    if item[0] in items.values():
        return (item[0], None)
    
    # If the item is not stored in a drawer, try to move it to its other drawer
    other_drawer = item[1] if item[0] == item[1] else item[0]
    if other_drawer not in items.values():
        return (other_drawer, None)
    
    # If the item cannot be moved to its other drawer, try to move it to the next drawer
    next_drawer = items[other_drawer][0]
    if next_drawer not in items.values():
        return (next_drawer, None)
    
    # If the item cannot be moved to the next drawer, throw it away
    return (None, None)

