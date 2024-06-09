
def solve(n, levels):
    # Initialize the minimum time to beat all levels as infinity
    min_time = float('inf')
    # Loop through each level
    for level in levels:
        # Get the shortcut item and completion time for the current level
        shortcut_item, shortcut_time = level[0], level[1]
        # Get the completion times for each item for the current level
        item_times = level[2:]
        # Initialize the minimum time to beat the current level as infinity
        min_time_level = float('inf')
        # Loop through each item for the current level
        for item in range(n+1):
            # If the item is the shortcut item, set the completion time to the shortcut time
            if item == shortcut_item:
                time = shortcut_time
            # Otherwise, set the completion time to the completion time for the item
            else:
                time = item_times[item]
            # If the completion time for the current item is less than the minimum time to beat the current level, update the minimum time
            if time < min_time_level:
                min_time_level = time
        # Add the minimum time to beat the current level to the total minimum time
        min_time += min_time_level
    # Return the total minimum time to beat all levels
    return min_time

