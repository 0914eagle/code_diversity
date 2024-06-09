
def solve(a):
    # Step 1: Find the minimum element in the list
    min_element = min(a)
    
    # Step 2: Create a dictionary to store the colors and the elements they are associated with
    colors = {}
    
    # Step 3: Iterate through the list and assign a color to each element
    for element in a:
        if element % min_element == 0:
            # If the element is divisible by the minimum element, assign it to the same color as the minimum element
            colors[element] = min_element
        else:
            # If the element is not divisible by the minimum element, create a new color and assign it to the element
            colors[element] = len(colors) + 1
    
    # Step 4: Return the number of colors used
    return len(set(colors.values()))

