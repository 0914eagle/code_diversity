
def solve(N, L, pairs):
    # Initialize a dictionary to store the items and their corresponding drawers
    items = {}
    for i in range(N):
        items[i+1] = pairs[i]
    
    # Initialize a list to store the items that will be stored successfully
    stored_items = []
    
    # Iterate through the items and apply the rules to store them
    for i in range(N):
        item = items[i+1]
        drawer_a, drawer_b = item[0], item[1]
        
        # If the drawer A is empty, store the item in that drawer
        if drawer_a not in stored_items:
            stored_items.append(drawer_a)
            print("LADICA")
            continue
        
        # If the drawer B is empty, store the item in that drawer
        if drawer_b not in stored_items:
            stored_items.append(drawer_b)
            print("LADICA")
            continue
        
        # If both drawers are filled, try to move the item to its other drawer
        other_drawer = drawer_a if drawer_b in stored_items else drawer_b
        if other_drawer not in stored_items:
            stored_items.append(other_drawer)
            print("LADICA")
            continue
        
        # If the item cannot be stored, throw it away
        print("SMECE")
    
    return stored_items

