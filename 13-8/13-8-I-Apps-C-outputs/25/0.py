
def num_ways(R, W, d):
    # Initialize the number of ways to be 1
    num_ways = 1
    
    # Loop through each type of wine
    for i in range(2):
        # Initialize the number of boxes of the current type to be R if it's the first type, and W if it's the second type
        num_boxes = R if i == 0 else W
        # Loop through each pile of the current type
        for j in range(num_boxes):
            # If the current pile is not the first pile, we need to consider the previous pile
            if j > 0:
                # If the previous pile is the same type as the current pile, we cannot place the current pile next to it
                if i == (j - 1) % 2:
                    num_ways -= 1
            # If the current pile is red, we need to ensure that it does not have more than d boxes
            if i == 0 and j > d:
                num_ways -= 1
    
    return num_ways % 1000000007

