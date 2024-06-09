
def is_wall_complete(heights):
    # Check if all parts of the wall have the same height
    if len(set(heights)) == 1:
        return True

    # Check if the wall has no empty spaces inside it
    for i in range(len(heights) - 1):
        if heights[i] != heights[i+1]:
            return False

    return True

