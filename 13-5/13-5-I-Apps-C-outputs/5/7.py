
def get_shortcut_time(level, shortcut_item, shortcut_time, item_times):
    # Find the index of the shortcut item in the item_times list
    shortcut_index = item_times.index(shortcut_item)
    
    # Get the completion time for the level using the shortcut
    shortcut_completion_time = item_times[shortcut_index]
    
    # Return the minimum of the shortcut completion time and the completion time for the level using any other item
    return min(shortcut_completion_time, shortcut_time)

def get_min_time(levels, item_times):
    # Initialize the minimum time to 0
    min_time = 0
    
    # Loop through the levels
    for level in levels:
        # Get the shortcut item and completion time for the level
        shortcut_item, shortcut_time = level[0], level[1]
        
        # Get the completion time for the level using the shortcut
        shortcut_completion_time = get_shortcut_time(level, shortcut_item, shortcut_time, item_times)
        
        # Add the completion time for the level to the minimum time
        min_time += shortcut_completion_time
    
    # Return the minimum time
    return min_time

def main():
    # Read the number of levels and the levels from stdin
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    
    # Get the item times from stdin
    item_times = list(map(int, input().split()))
    
    # Get the minimum time to beat all the levels
    min_time = get_min_time(levels, item_times)
    
    # Print the minimum time
    print(min_time)

if __name__ == '__main__':
    main()

