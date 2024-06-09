
def get_shortcut_time(level, shortcut, items):
    # Find the index of the shortcut item in the items list
    shortcut_index = items.index(shortcut)
    # Return the minimum time to complete the level using the shortcut item or any of the other items
    return min(items[shortcut_index], *[items[i] for i in range(shortcut_index)])

def get_min_time(levels, items):
    # Initialize the minimum time to complete all levels to 0
    min_time = 0
    # Loop through each level
    for level in levels:
        # Get the shortcut time for the current level
        shortcut_time = get_shortcut_time(level, level[0], level[1:])
        # Add the shortcut time to the minimum time
        min_time += shortcut_time
    # Return the minimum time to complete all levels
    return min_time

def main():
    # Read the number of levels and the levels from stdin
    n = int(input())
    levels = []
    for _ in range(n):
        levels.append(list(map(int, input().split())))
    # Get the minimum time to complete all levels
    min_time = get_min_time(levels, range(n+1))
    # Print the minimum time
    print(min_time)

if __name__ == '__main__':
    main()

