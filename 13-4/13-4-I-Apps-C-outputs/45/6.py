
def solve(a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the number of colors as 1
    colors = 1
    # Initialize the current color as 1
    color = 1
    # Loop through the array
    for i in range(1, len(a)):
        # If the current element is not divisible by the previous element, increase the color count and the current color
        if a[i] % a[i-1] != 0:
            colors += 1
            color += 1
        # Assign the current color to the current element
        a[i] = color
    # Return the minimum number of colors needed
    return colors

