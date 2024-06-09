
def solve(a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of colors as 1
    min_colors = 1
    # Initialize the current color as 1
    color = 1
    # Iterate through the array
    for i in range(1, len(a)):
        # If the current element is not divisible by the previous element, increment the color
        if a[i] % a[i-1] != 0:
            color += 1
        # Update the minimum number of colors
        min_colors = max(min_colors, color)
    # Return the minimum number of colors
    return min_colors

