
def solve(a):
    # Step 1: Find the minimal element in the sequence
    minimal_element = min(a)
    
    # Step 2: Create a dictionary to store the colors and their corresponding elements
    colors = {}
    
    # Step 3: Iterate through the sequence and assign elements to colors
    for element in a:
        if element % minimal_element == 0:
            # If the element is divisible by the minimal element, assign it to the first color
            if 1 not in colors:
                colors[1] = [element]
            else:
                colors[1].append(element)
        else:
            # If the element is not divisible by the minimal element, assign it to a new color
            current_color = max(colors.keys()) + 1
            colors[current_color] = [element]
    
    # Step 4: Return the number of colors used
    return len(colors)

