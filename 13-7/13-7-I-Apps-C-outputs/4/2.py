
def solve(a):
    # Sort the array in ascending order
    a.sort()
    
    # Initialize the minimum number of colors to 1
    min_colors = 1
    
    # Iterate over the array
    for i in range(1, len(a)):
        # If the current element is not divisible by the previous element, we need to use another color
        if a[i] % a[i-1] != 0:
            min_colors += 1
    
    return min_colors

