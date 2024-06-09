
def get_color_choices(n, k):
    # Initialize a list to store the color choices
    color_choices = []
    
    # Iterate through each pair
    for i in range(n):
        # Get the color choices for the current pair
        b, g = get_color_choice(k)
        
        # Add the color choices to the list
        color_choices.append((b, g))
    
    # Return the list of color choices
    return color_choices

def get_color_choice(k):
    # Initialize a list to store the color choices
    color_choices = []
    
    # Iterate through each color
    for i in range(k):
        # Check if the color is already in the list
        if i not in color_choices:
            # Add the color to the list
            color_choices.append(i)
    
    # Return a random color choice from the list
    return random.choice(color_choices), random.choice(color_choices)

if __name__ == '__main__':
    n, k = map(int, input().split())
    color_choices = get_color_choices(n, k)
    print("YES")
    for b, g in color_choices:
        print(b, g)

