
def solve(n, a):
    # Calculate the total height of the fence
    total_height = sum(a)

    # Initialize the minimum number of strokes to paint the fence
    min_strokes = 0

    # Iterate through each plank of the fence
    for i in range(n):
        # Calculate the height of the current plank
        current_height = a[i]

        # If the current plank is higher than the total height of the fence, return -1
        if current_height > total_height:
            return -1

        # If the current plank is equal to the total height of the fence, return the current stroke number
        if current_height == total_height:
            return min_strokes + 1

        # Calculate the remaining height of the fence after painting the current plank
        remaining_height = total_height - current_height

        # If the remaining height is zero, return the current stroke number
        if remaining_height == 0:
            return min_strokes + 1

        # Calculate the minimum number of strokes needed to paint the remaining height
        min_strokes_remaining = (remaining_height - 1) // current_height + 1

        # Update the minimum number of strokes to paint the fence
        min_strokes += min_strokes_remaining

    # If the fence cannot be painted using the given brush width, return -1
    return -1

