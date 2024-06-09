
def solve(a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the number of colors as 1
    colors = 1
    # Loop through the array
    for i in range(1, len(a)):
        # If the current element is not divisible by the previous element, increment the number of colors
        if a[i] % a[i-1] != 0:
            colors += 1
    return colors

