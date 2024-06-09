
def solve(n, a):
    # Calculate the total height of the fence
    total_height = sum(a)

    # Initialize the minimum number of strokes to paint the fence
    min_strokes = 0

    # Iterate through each plank of the fence
    for i in range(n):
        # Calculate the height of the current plank
        current_height = a[i]

        # Check if the current plank is higher than the total height of the fence
        if current_height > total_height:
            # If it is, add the difference to the minimum number of strokes
            min_strokes += current_height - total_height

            # Break the loop, as we can't paint the rest of the fence
            break

        # Otherwise, subtract the height of the current plank from the total height
        total_height -= current_height

    # Return the minimum number of strokes needed to paint the fence
    return min_strokes

