
def paint_fence(planks):
    # Calculate the total height of the fence
    total_height = sum(planks)

    # Initialize the minimum number of strokes to paint the fence
    min_strokes = 0

    # Iterate through the planks and calculate the minimum number of strokes to paint each plank
    for plank in planks:
        min_strokes += (total_height // plank) + (1 if total_height % plank > 0 else 0)

    return min_strokes

