
def get_min_colors(a):
    # Sort the list in ascending order
    a.sort()
    # Initialize the minimum number of colors as 1
    min_colors = 1
    # Loop through the list and check if the current element is divisible by the previous element
    for i in range(1, len(a)):
        if a[i] % a[i-1] != 0:
            # If the current element is not divisible by the previous element, increment the minimum number of colors
            min_colors += 1
    return min_colors

