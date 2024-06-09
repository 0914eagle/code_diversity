
def paint_fence(planks, heights):
    # Calculate the total height of the fence
    total_height = sum(heights)

    # Initialize the number of strokes to 0
    strokes = 0

    # Iterate through the planks and heights
    for i in range(len(planks)):
        # Check if the current plank is the last one
        if i == len(planks) - 1:
            # If it is the last plank, we can paint it with a vertical stroke
            strokes += 1
        else:
            # If it is not the last plank, we need to check if the next plank has a higher height
            if heights[i] < heights[i + 1]:
                # If the next plank has a higher height, we can paint both planks with a horizontal stroke
                strokes += 1
            else:
                # If the next plank has a lower or equal height, we can paint the current plank with a vertical stroke
                strokes += 1

    return strokes

