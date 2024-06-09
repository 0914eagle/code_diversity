
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

        # If the current plank is equal to the total height of the fence, return the current stroke count
        if current_height == total_height:
            return min_strokes + 1

        # Calculate the height of the remaining fence after painting the current plank
        remaining_height = total_height - current_height

        # If the remaining height is divisible by the current plank's height, add one stroke to the minimum number of strokes
        if remaining_height % current_height == 0:
            min_strokes += 1

    # Return the minimum number of strokes to paint the fence
    return min_strokes

