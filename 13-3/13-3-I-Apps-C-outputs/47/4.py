
def solve(n, levels):
    # Initialize the minimum time to beat all levels
    min_time = 0
    # Initialize the inventory with item 0
    inventory = [0]
    # Loop through each level
    for level in levels:
        # Get the shortcut item and completion time for the current level
        shortcut_item, completion_time = level[0], level[1]
        # Get the completion times for each item
        item_times = level[2:]
        # Check if the shortcut item is already in the inventory
        if shortcut_item in inventory:
            # If the shortcut item is already in the inventory, use it to complete the level
            min_time += completion_time
        else:
            # If the shortcut item is not in the inventory, find the minimum completion time among all items
            min_time += min(item_times)
        # Add the shortcut item to the inventory
        inventory.append(shortcut_item)
    return min_time

