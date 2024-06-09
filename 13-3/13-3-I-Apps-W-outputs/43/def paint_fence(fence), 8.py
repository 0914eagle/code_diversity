
def paint_fence(fence):
    # Calculate the total height of the fence
    total_height = sum(fence)

    # Initialize the number of strokes to 0
    strokes = 0

    # Iterate through the fence planks
    for i in range(len(fence)):
        # Check if the current plank is the last one
        if i == len(fence) - 1:
            # If it is the last plank, we only need to paint it if it is not already painted
            if fence[i] > 0:
                strokes += 1
        else:
            # If it is not the last plank, we need to paint it if it is not already painted and the next plank is not already painted
            if fence[i] > 0 and fence[i + 1] > 0:
                strokes += 1

    return strokes

