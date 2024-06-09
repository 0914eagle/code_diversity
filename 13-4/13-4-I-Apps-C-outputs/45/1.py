
def solve(a):
    # Step 1: Find the minimum element in the list
    min_element = min(a)
    
    # Step 2: Create a dictionary to store the colors
    colors = {}
    
    # Step 3: Iterate through the list and assign colors to elements
    for element in a:
        if element % min_element == 0:
            # If the element is divisible by the minimum element, assign it the same color as the minimum element
            colors[element] = min_element
        else:
            # If the element is not divisible by the minimum element, create a new color for it
            colors[element] = len(colors) + 1
    
    # Step 4: Return the number of colors used
    return len(set(colors.values()))

