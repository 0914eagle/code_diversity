
def is_vova_wall_complete(wall_heights):
    # Check if the wall is already complete
    if all(wall_heights[0] == height for height in wall_heights):
        return True

    # Check if the wall can be completed using any amount of bricks
    for i in range(len(wall_heights) - 1):
        if wall_heights[i] == wall_heights[i + 1]:
            return True

    return False

