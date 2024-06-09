
def solve(a):
    # Step 1: Find the minimum element in the list
    min_element = min(a)
    
    # Step 2: Create a dictionary to store the colors and their corresponding elements
    colors = {}
    
    # Step 3: Iterate through the list and assign elements to colors
    for element in a:
        if element % min_element == 0:
            # If the element is divisible by the minimum element, assign it to the first color
            if 1 not in colors:
                colors[1] = [element]
            else:
                colors[1].append(element)
        else:
            # If the element is not divisible by the minimum element, assign it to the next color
            for i in range(2, len(colors) + 2):
                if i not in colors:
                    colors[i] = [element]
                    break
                else:
                    colors[i].append(element)
    
    # Step 4: Return the number of colors used
    return len(colors)

