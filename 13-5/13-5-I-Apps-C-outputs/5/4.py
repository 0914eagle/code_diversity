
def get_shortcut_time(level, shortcut_item, completion_time, items):
    # Find the index of the shortcut item in the items list
    shortcut_index = items.index(shortcut_item)
    # Get the completion time for the level using the shortcut item
    shortcut_time = completion_time[shortcut_index]
    # Get the completion time for the level using the other items
    other_times = [completion_time[i] for i in range(len(completion_time)) if i != shortcut_index]
    # Return the minimum of the shortcut time and the other times
    return min(shortcut_time, *other_times)

def get_min_time(levels):
    # Initialize the minimum time to 0
    min_time = 0
    # Loop through the levels
    for level in levels:
        # Get the shortcut item, completion time, and items for the level
        shortcut_item, completion_time, items = level
        # Get the shortcut time for the level
        shortcut_time = get_shortcut_time(level, shortcut_item, completion_time, items)
        # Add the shortcut time to the minimum time
        min_time += shortcut_time
    # Return the minimum time
    return min_time

if __name__ == '__main__':
    levels = []
    for _ in range(int(input())):
        levels.append(list(map(int, input().split())))
    print(get_min_time(levels))

