
def get_min_spots(n, H):
    # Initialize the height of the first pillar as 1
    height = 1
    # Initialize the number of spots as 1
    spots = 1
    # Loop through the remaining sand packs
    for i in range(n-1):
        # If the height of the previous pillar is less than or equal to the height of the fence, increase the height of the current pillar by 1
        if height <= H:
            height += 1
        # Otherwise, increase the number of spots by 1 and set the height of the current pillar to 1
        else:
            spots += 1
            height = 1
    return spots

