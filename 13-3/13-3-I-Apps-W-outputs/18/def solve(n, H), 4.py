
def solve(n, H):
    # Initialize the height of the castle as 1
    height = 1
    
    # Initialize the number of spots as 1
    spots = 1
    
    # While there is still sand left to use
    while n > 0:
        # If the current height is less than or equal to the fence height
        if height <= H:
            # Add the current height to the total height of the castle
            height += 1
            # Subtract the current height from the total number of sand packs
            n -= height
        # If the current height is greater than the fence height
        else:
            # Add the current height to the total number of spots occupied
            spots += 1
            # Subtract the current height from the total number of sand packs
            n -= height
            # Reset the height to 1 for the next spot
            height = 1
    
    # Return the minimum number of spots required to build the castle
    return spots

