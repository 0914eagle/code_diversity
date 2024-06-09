
def get_largest_connected_group(forest):
    # Initialize a list to store the heights of the trees
    heights = []
    
    # Iterate over the forest matrix and append the height of each tree to the list
    for row in forest:
        for tree in row:
            heights.append(tree[0])
    
    # Sort the list of heights in descending order
    heights.sort(reverse=True)
    
    # Initialize a dictionary to store the heights as keys and the number of trees as values
    height_count = {}
    
    # Iterate over the list of heights and increment the value of the corresponding key in the dictionary
    for height in heights:
        if height in height_count:
            height_count[height] += 1
        else:
            height_count[height] = 1
    
    # Initialize a maximum value to store the largest connected group
    max_group = 0
    
    # Iterate over the dictionary and find the key with the maximum value
    for key, value in height_count.items():
        if value > max_group:
            max_group = value
    
    return max_group

