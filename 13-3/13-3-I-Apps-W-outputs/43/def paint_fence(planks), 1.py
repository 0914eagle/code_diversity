
def paint_fence(planks):
    # Calculate the total height of the fence
    total_height = sum(planks)

    # Initialize the number of strokes to 0
    strokes = 0

    # Iterate through the planks
    for i in range(len(planks)):
        # Check if the current plank is the last one
        if i == len(planks) - 1:
            # If it is the last plank, break the loop
            break

        # Calculate the height of the current plank
        current_height = planks[i]

        # Calculate the height of the next plank
        next_height = planks[i + 1]

        # Check if the current plank is higher than the next plank
        if current_height > next_height:
            # If it is, increase the number of strokes by 1
            strokes += 1

    # Return the total number of strokes needed to paint the fence
    return strokes

