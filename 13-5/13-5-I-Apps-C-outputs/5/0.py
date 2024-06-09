
def get_completion_time(levels, shortcut_item, shortcut_time, items):
    # Initialize the minimum completion time for each level
    completion_time = [float('inf') for _ in range(len(levels) + 1)]
    completion_time[0] = 0
    
    # Loop through each level
    for level in range(1, len(levels) + 1):
        # Get the completion times for each item
        item_completion_times = items[level - 1]
        
        # Check if the shortcut item is available for this level
        if shortcut_item[level - 1] != 0:
            # Add the shortcut time to the minimum completion time
            completion_time[level] = min(completion_time[level], completion_time[shortcut_item[level - 1]] + shortcut_time[level - 1])
        
        # Loop through each item and check if it's faster than the current minimum completion time
        for item in range(1, len(items) + 1):
            if item_completion_times[item - 1] < completion_time[level]:
                completion_time[level] = min(completion_time[level], completion_time[item - 1] + item_completion_times[item - 1])
    
    return completion_time[-1]

def main():
    levels, shortcut_item, shortcut_time, items = read_input()
    print(get_completion_time(levels, shortcut_item, shortcut_time, items))

def read_input():
    levels = int(input())
    shortcut_item = []
    shortcut_time = []
    items = []
    for _ in range(levels):
        shortcut_item.append(int(input()))
        shortcut_time.append(int(input()))
        items.append(list(map(int, input().split())))
    return levels, shortcut_item, shortcut_time, items

if __name__ == '__main__':
    main()

