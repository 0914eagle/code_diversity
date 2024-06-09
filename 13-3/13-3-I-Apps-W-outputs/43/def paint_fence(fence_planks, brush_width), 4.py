
def paint_fence(fence_planks, brush_width):
    # Calculate the total width of the fence
    total_width = sum(fence_planks)
    
    # Calculate the minimum number of strokes needed to paint the fence
    num_strokes = total_width // brush_width
    
    # If the total width is not evenly divisible by the brush width, add an extra stroke
    if total_width % brush_width != 0:
        num_strokes += 1
    
    return num_strokes

